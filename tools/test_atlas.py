import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import graph as G  # noqa: E402
import import_la  # noqa: E402


class GraphTest(unittest.TestCase):
    # a -> b -> d, a -> c -> d, a -> d (shortcut)
    P = {"a": set(), "b": {"a"}, "c": {"a"}, "d": {"a", "b", "c"}}

    def test_topo(self):
        order = G.topo_order(self.P)
        for n, ps in self.P.items():
            for p in ps:
                self.assertLess(order.index(p), order.index(n))

    def test_cycle(self):
        self.assertIsNone(G.find_cycle(self.P))
        cyc = G.find_cycle({"x": {"y"}, "y": {"x"}})
        self.assertEqual(cyc[0], cyc[-1])
        with self.assertRaises(ValueError):
            G.topo_order({"x": {"y"}, "y": {"x"}})

    def test_closures(self):
        self.assertEqual(G.ancestors(self.P, ["d"]), {"a", "b", "c", "d"})
        self.assertEqual(G.descendants(self.P, ["b"]), {"b", "d"})

    def test_longest(self):
        height, back = G.longest_paths(self.P)
        self.assertEqual(height["d"], 3)
        self.assertEqual(len(G.path_to(back, "d")), 3)

    def test_reduction_drops_shortcut_only(self):
        red = G.transitive_reduction(self.P)
        self.assertEqual(red["d"], {"b", "c"})
        self.assertEqual(red["b"], {"a"})


class ImportLATest(unittest.TestCase):
    def test_section_mapping(self):
        f = import_la.atlas_chapter
        self.assertEqual(f("ch00-foundations/10-groups.html"), "AL1.1")
        self.assertEqual(f("ch07-determinants/03-x.html"), "LA2.7")
        self.assertEqual(f("ch24-applied/01-x.html"), "NLA.24")
        self.assertIsNone(f("ch24a-notation/index.html"))

    def test_edge_policy(self):
        labels = {
            "thm-a": {"file": "ch01-vector-spaces/01-x.html", "uses": [], "uses_kinds": {}},
            "thm-b": {"file": "ch02-linear-maps/01-x.html", "uses": ["thm-a"], "uses_kinds": {"thm-a": ["proof"]}},
            "thm-c": {"file": "ch03-linear-systems/01-x.html", "uses": ["thm-a"], "uses_kinds": {"thm-a": ["remark"]}},
            "thm-d": {"file": "ch04-matrices/01-x.html", "optional": True, "uses": ["thm-a"],
                      "uses_kinds": {"thm-a": ["proof"]}},
        }
        edges, _ = import_la.compute(labels)
        got = {(e[0], e[1]): e[2] for e in edges}
        self.assertEqual(got[("LA1.2", "LA1.1")], "s")
        self.assertEqual(got[("LA1.3", "LA1.1")], "see")
        self.assertEqual(got[("LA1.4", "LA1.1")], "see")  # citations from optional results are soft

    def test_moves(self):
        labels = {
            "thm-m": {"file": "ch12-spectral/01-x.html", "uses": [], "uses_kinds": {}},
            "thm-u": {"file": "ch21-inequalities/01-x.html", "uses": ["thm-m"], "uses_kinds": {"thm-m": ["proof"]}},
        }
        moves = {"thm-m": {"to": "AN3.3", "borrowed_by": ["MA.21"]}}
        edges, _ = import_la.compute(labels, moves)
        got = {(e[0], e[1]): e[2] for e in edges}
        self.assertEqual(got, {("MA.21", "AN3.3"): "b"})

    def test_softened_for(self):
        labels = {
            "thm-l": {"file": "ch21-inequalities/10-x.html", "uses": [], "uses_kinds": {}},
            "cor-c": {"file": "ch21-inequalities/10-x.html", "uses": ["thm-l"], "uses_kinds": {"thm-l": ["proof"]}},
        }
        moves = {"thm-l": {"to": "MA.21b", "softened_for": ["MA.21"]}}
        edges, _ = import_la.compute(labels, moves)
        self.assertEqual({(e[0], e[1]): e[2] for e in edges}, {("MA.21", "MA.21b"): "see"})

    def test_vocabulary(self):
        labels = {
            "def-a": {"file": "ch01-x/01-x.html", "uses": [], "uses_kinds": {}},
            "def-b": {"file": "ch02-x/01-x.html", "uses": ["def-a"], "uses_kinds": {"def-a": ["definition"]}},
            "thm-t": {"file": "ch03-x/01-x.html", "uses": ["def-b", "def-a"],
                      "uses_kinds": {"def-b": ["theorem"], "def-a": ["proof"]}},
            "thm-u": {"file": "ch04-x/01-x.html", "uses": ["thm-t"], "uses_kinds": {"thm-t": ["proof"]}},
        }
        got = {(to, frm, kind) for to, frm, kind, _ in import_la.vocabulary(labels)}
        # LA1.4 borrows thm-t: it needs the words of thm-t's statement (LA1.2), not LA1.3 itself
        self.assertIn(("LA1.4", "LA1.2", "all"), got)
        self.assertNotIn(("LA1.4", "LA1.3", "all"), got)
        self.assertIn(("LA1.2", "LA1.1", "stmt"), got)
        self.assertNotIn(("LA1.3", "LA1.1", "stmt"), got)  # cited from the proof only


class RegistryTest(unittest.TestCase):
    def test_registry_passes_check(self):
        import atlas
        at = atlas.Atlas()
        self.assertTrue(atlas.check(at), at.errors)

    def test_borrow_lints(self):
        import atlas
        at = atlas.Atlas()
        at.scope[("MA.21", "AN3.3")] = ["AN3.1"]  # MA readers never read multivariable calculus
        at.statements["edges"].append(["thm-zorn", "def-ac", "borrows", "A1/R2"])
        self.assertFalse(atlas.check(at))
        self.assertTrue(any(e.startswith("scope lint: MA.21") for e in at.errors), at.errors)
        self.assertTrue(any("a borrow needs at most R1" in e for e in at.errors), at.errors)

    def test_cycle_through_optional_chapters_is_an_error(self):
        import atlas
        at = atlas.Atlas()
        at.edges[("MA.21", "MA.21b")] = "s"  # MA.21b already s-depends on MA.21
        self.assertFalse(atlas.check(at))
        self.assertTrue(any(e.startswith("s ∪ b has a cycle") for e in at.errors), at.errors)

    def test_stale_and_unlinked_overrides(self):
        import atlas
        at = atlas.Atlas()
        at.overrides = [o if o[1] != "softened_for" else (o[0], o[1], o[2], 0) for o in at.overrides]
        at.moves[0] = dict(at.moves[0], todo="no-such-item")
        self.assertFalse(atlas.check(at))
        self.assertTrue(any(e.startswith("stale override in moves.yaml[thm-loewner]") for e in at.errors), at.errors)
        self.assertTrue(any("todo:no-such-item is not an open item" in e for e in at.errors), at.errors)

    def test_effects_count(self):
        labels = {
            "thm-l": {"file": "ch21-inequalities/10-x.html", "uses": [], "uses_kinds": {}},
            "cor-c": {"file": "ch21-inequalities/10-x.html", "uses": [], "uses_kinds": {}},
        }
        effects = {}
        import_la.compute(labels, {"thm-l": {"to": "MA.21b", "softened_for": ["MA.21"]}}, effects)
        self.assertEqual(effects, {("thm-l", "softened_for", "MA.21"): 0})  # the rewrite is done: stale

    def test_terms_and_local_definitions(self):
        import atlas
        at = atlas.Atlas()
        nodes, edges = at.statements["nodes"], at.statements["edges"]
        nodes.append(["def-x-cont", "MA.17", "def", "second definition", "A1", "R1", "continuous"])
        for i in range(3):  # LA2.10 already defines three terms in place
            nodes.append([f"def-x-extra{i}", "LA2.10", "def", "extra", "A1", "R1", "continuous"])
            edges.append([f"def-x-extra{i}", "def-continuous", "specializes"])
        nodes.append(["def-x-deep", "LA2.6", "def", "too deep", "A1", "R2", "derivative"])
        edges.append(["def-x-deep", "def-derivative", "specializes"])
        self.assertFalse(atlas.check(at))
        self.assertTrue(any(e.startswith("term `continuous` has 2 definitions") for e in at.errors), at.errors)
        self.assertTrue(any(e.startswith("LA2.10 defines 6 terms in place") for e in at.errors), at.errors)
        self.assertTrue(any(e.startswith("local definition def-x-deep is taught at R2") for e in at.errors), at.errors)

    def test_generalization_must_be_linked(self):
        import atlas
        at = atlas.Atlas()
        del at.edges[("AN3.7", "MT.6")]  # Stokes on manifolds vs the divergence theorem
        self.assertFalse(atlas.check(at))
        self.assertTrue(any("thm-stokes (AN3.7) generalizes" in e for e in at.errors), at.errors)

    def test_computed_replaces_plan_where_written(self):
        import atlas
        at = atlas.Atlas()
        at.plan[("LA1.4", "MA.20")] = ("s", None)  # a stale planned s edge between written chapters
        at.plan[("LA3.11", "MA.16")] = ("see", None)  # a planned pointer the proofs do not contradict
        at.plan[("AN3.1", "MA.16")] = ("s", None)  # AN3 is not written: the plan stands
        eff = at._merge()
        self.assertNotIn(("LA1.4", "MA.20"), at.computed)
        self.assertNotIn(("LA1.4", "MA.20"), eff)
        self.assertEqual(eff.get(("LA3.11", "MA.16")), "see")
        self.assertEqual(eff.get(("AN3.1", "MA.16")), "s")

    def test_constraints_only_on_unwritten_chapters(self):
        import atlas
        at = atlas.Atlas()
        at.constraints.append({"chapter": "LA2.6", "decided": "2026-10-09", "rule": "define continuity in place"})
        self.assertFalse(atlas.check(at))
        self.assertTrue(any(e.startswith("chapter-constraints.yaml: LA2.6 is already written") for e in at.errors), at.errors)

    def test_subject_after(self):
        import atlas
        at = atlas.Atlas()
        s_only = at.preds({"s"})
        alone = atlas.G.ancestors(s_only, at.subject["ergodic-theory"]["hook"])
        subj, entry = atlas.subject_entry(at, ["ergodic-theory"], s_only)
        self.assertEqual(subj, {"ergodic-theory", "dynamical-systems"})
        self.assertIn("AN2.4", entry - alone)  # the dynamical-systems hook comes in through after
        at.subject["dynamical-systems"]["after"] = ["ergodic-theory"]
        self.assertFalse(atlas.check(at))
        self.assertTrue(any(e.startswith("fields.yaml: subject-level after cycle") for e in at.errors), at.errors)

    def test_field_deviations_new_and_stale(self):
        import atlas
        at = atlas.Atlas()
        del at.subject["ergodic-theory"]["after"]
        at.deviations.append({"key": "erg <- calc", "why": "test"})
        self.assertTrue(atlas.check(at), at.errors)
        self.assertTrue(any("new deviations" in w and "erg <- dyn" in w for w in at.warnings), at.warnings)
        self.assertTrue(any(w.startswith("field-deviations.yaml: erg <- calc no longer occurs") for w in at.warnings), at.warnings)


if __name__ == "__main__":
    unittest.main()
