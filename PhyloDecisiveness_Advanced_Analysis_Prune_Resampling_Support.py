Here are five advanced code examples related to **"Checking Phylogenetic Decisiveness in Theory and in Practice"**, focusing on phylogenetic tree analysis, decisiveness metrics, and computational algorithms to determine the robustness of phylogenetic methods. These examples use specific data, accurate structuring, and clear answers while employing a holistic strategy for solving practical problems in phylogenetics.

### 1. **Building a Phylogenetic Tree from a Sequence Alignment**
This example demonstrates how to construct a phylogenetic tree from sequence alignment data using a distance-based method like Neighbor-Joining (NJ).

```python
from Bio import Phylo
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor
from Bio.Align import MultipleSeqAlignment
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from io import StringIO

# Create an example sequence alignment
alignment_data = """\
>P1
ATCGTACGATCG
>P2
ATCGTACGTAGG
>P3
ATCGTTCGATCG
>P4
ATCGTACGGTCC
"""
alignment = MultipleSeqAlignment([
    SeqRecord(Seq("ATCGTACGATCG"), id="P1"),
    SeqRecord(Seq("ATCGTACGTAGG"), id="P2"),
    SeqRecord(Seq("ATCGTTCGATCG"), id="P3"),
    SeqRecord(Seq("ATCGTACGGTCC"), id="P4")
])

# Calculate the distance matrix
calculator = DistanceCalculator('identity')
dm = calculator.get_distance(alignment)

# Construct the tree using Neighbor-Joining (NJ) algorithm
constructor = DistanceTreeConstructor(calculator, 'nj')
tree = constructor.build_tree(alignment)

# Visualize the tree
Phylo.draw_ascii(tree)
```

**Value**: This code provides the foundation for building a phylogenetic tree from sequence alignment, which is the starting point for assessing phylogenetic decisiveness.

---

### 2. **Computing Phylogenetic Decisiveness for a Set of Trees**
This example computes phylogenetic decisiveness by evaluating whether a set of phylogenetic trees resolves the relationships among all taxa under different criteria.

```python
import itertools

# Function to check decisiveness for a set of trees
def is_decisive(taxa_sets, tree_set):
    decisive = True
    for taxa in taxa_sets:
        resolved = any(tree.is_resolved(taxa) for tree in tree_set)
        if not resolved:
            decisive = False
            break
    return decisive

# Example taxa and trees (simplified)
taxa_sets = [('P1', 'P2', 'P3'), ('P2', 'P3', 'P4')]
tree_set = [tree1, tree2, tree3]  # Placeholder trees

# Check decisiveness
decisiveness = is_decisive(taxa_sets, tree_set)
print(f"Is the set of trees decisive? {'Yes' if decisiveness else 'No'}")
```

**Value**: This example introduces a key concept of phylogenetic decisiveness, determining whether the set of phylogenetic trees can decisively resolve all taxa relationships.

---

### 3. **Assessing Decisiveness Using Bootstrap Resampling**
This code uses bootstrap resampling to generate multiple phylogenetic trees from sequence data and assess how often the trees are decisive for a given taxa set.

```python
from Bio import AlignIO
from Bio.Phylo.TreeConstruction import Bootstrap

# Load the sequence alignment
alignment = AlignIO.read("sequence_alignment.fasta", "fasta")

# Perform bootstrap resampling to generate multiple trees
constructor = DistanceTreeConstructor(DistanceCalculator('identity'))
bootstrap = Bootstrap(alignment, constructor, reps=100)
bootstrap_trees = bootstrap.bootstrap()

# Evaluate decisiveness for each bootstrap tree
decisive_trees = [is_decisive(taxa_sets, [tree]) for tree in bootstrap_trees]

# Calculate the percentage of decisive trees
decisive_percentage = sum(decisive_trees) / len(bootstrap_trees) * 100
print(f"Percentage of decisive trees: {decisive_percentage:.2f}%")
```

**Value**: Bootstrap resampling is widely used in phylogenetics to evaluate the robustness of tree topologies. This example extends it to test decisiveness, giving a quantitative measure of decisiveness across resampled trees.

---

### 4. **Visualizing Tree Support with Phylogenetic Decisiveness**
This example visualizes the support values (e.g., bootstrap support) for each clade in the tree and overlays decisiveness information.

```python
from Bio.Phylo import draw

# Load the tree and bootstrap support values
tree = Phylo.read("phylo_tree.xml", "phyloxml")

# Overlay bootstrap values and decisiveness on the tree
for clade in tree.find_clades():
    if clade.confidence:
        clade.name = f"{clade.name} ({clade.confidence:.1f})"
        if is_decisive([clade.name], [tree]):
            clade.color = 'green'
        else:
            clade.color = 'red'

# Visualize the tree with decisiveness and support values
draw(tree)
```

**Value**: This example combines bootstrap support with phylogenetic decisiveness, helping researchers visually assess which parts of the tree are robust and decisive.

---

### 5. **Maximizing Phylogenetic Decisiveness by Pruning Non-Informative Taxa**
This code dynamically prunes non-informative taxa from the phylogenetic tree to maximize decisiveness, improving clarity in practical tree inference.

```python
# Prune non-informative taxa to increase decisiveness
def prune_non_informative(tree, taxa_sets):
    for clade in list(tree.find_clades()):
        taxa_in_clade = set([t.name for t in clade.get_terminals()])
        if all(taxa in taxa_in_clade for taxa in taxa_sets):
            tree.prune(clade)
    return tree

# Apply pruning to maximize decisiveness
pruned_tree = prune_non_informative(tree, taxa_sets)

# Check decisiveness of the pruned tree
decisiveness = is_decisive(taxa_sets, [pruned_tree])
print(f"Decisiveness after pruning: {'Yes' if decisiveness else 'No'}")

# Visualize the pruned tree
Phylo.draw(pruned_tree)
```

**Value**: This example maximizes phylogenetic decisiveness by removing non-informative taxa, ensuring that the final tree resolves critical relationships clearly, enhancing practical phylogenetic inference.

---

### **Smart File Name Suggestion**
`PhyloDecisiveness_Advanced_Analysis_Prune_Resampling_Support.py`

This file name captures the essence of advanced phylogenetic decisiveness analysis, with a focus on practical methods such as pruning, resampling, and support visualization.

---

These five advanced examples provide robust, data-driven solutions to assess and enhance phylogenetic decisiveness, combining theoretical insights with practical implementations for real-world biological data.
