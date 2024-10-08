Here are **five additional advanced and complementary code examples** related to "Checking Phylogenetic Decisiveness in Theory and in Practice," with deeper analysis, richer data structures, and enhanced computational approaches. These examples are designed to expand on the original set with more sophisticated methods, building on data-driven decision-making, tree optimization, and theoretical insights into phylogenetic analysis.

---

### 1. **Computing Phylogenetic Diversity for Multiple Trees**
This example calculates the phylogenetic diversity (PD) across multiple trees and taxa sets to assess the evolutionary information captured by the trees, giving a deeper look into the richness of evolutionary history represented.

```python
from Bio.Phylo.BaseTree import Clade

# Function to compute Phylogenetic Diversity (PD)
def compute_pd(tree, taxa_set):
    pd = 0
    for clade in tree.find_clades(order="level"):
        descendants = set([t.name for t in clade.get_terminals()])
        if any(taxon in descendants for taxon in taxa_set):
            pd += clade.branch_length if clade.branch_length else 0
    return pd

# Example taxa sets and trees
taxa_sets = [('P1', 'P2'), ('P3', 'P4')]
trees = [tree1, tree2]  # Placeholder trees with branch lengths

# Calculate PD for each tree and taxa set
for i, taxa_set in enumerate(taxa_sets):
    pd_values = [compute_pd(tree, taxa_set) for tree in trees]
    print(f"Phylogenetic Diversity for Taxa Set {i + 1}: {pd_values}")
```

**Value**: This example enhances phylogenetic decisiveness analysis by incorporating the concept of phylogenetic diversity (PD), which measures the evolutionary breadth captured by the trees, complementing decisiveness by assessing evolutionary richness.

---

### 2. **Optimizing Tree Space Search with Simulated Annealing**
This example uses simulated annealing to explore the space of phylogenetic trees, optimizing the tree structures for maximum decisiveness and resolving conflicts between different tree topologies.

```python
import random
import math

# Simulated Annealing to search for optimal tree
def simulated_annealing(initial_tree, taxa_sets, max_iterations=1000, temperature=100):
    current_tree = initial_tree
    current_score = compute_decisiveness_score(current_tree, taxa_sets)
    
    for i in range(max_iterations):
        new_tree = perturb_tree(current_tree)
        new_score = compute_decisiveness_score(new_tree, taxa_sets)
        delta = new_score - current_score
        
        if delta > 0 or random.random() < math.exp(delta / temperature):
            current_tree, current_score = new_tree, new_score
        
        temperature *= 0.99  # Reduce temperature over time

    return current_tree

# Example usage with initial tree
optimized_tree = simulated_annealing(initial_tree, taxa_sets)
print(f"Optimized Decisiveness Score: {compute_decisiveness_score(optimized_tree, taxa_sets)}")
```

**Value**: Simulated annealing provides a powerful optimization tool for exploring the space of possible tree topologies, allowing for the discovery of tree structures that maximize phylogenetic decisiveness while resolving potential conflicts.

---

### 3. **Using Bayesian Inference to Estimate Tree Decisiveness**
This example applies Bayesian inference to estimate the posterior probability distribution of tree topologies and assesses decisiveness based on the resulting probability distribution, adding probabilistic depth to the decisiveness analysis.

```python
from Bio.Phylo.TreeConstruction import BayesianTreeConstructor

# Set up Bayesian inference for phylogenetic tree estimation
def perform_bayesian_inference(alignment, taxa_sets):
    constructor = BayesianTreeConstructor()  # Placeholder Bayesian constructor
    tree, posterior = constructor.build_tree(alignment)  # Obtain tree and posterior probabilities
    
    decisive_probability = compute_decisiveness_probability(tree, taxa_sets, posterior)
    return tree, decisive_probability

# Placeholder function to compute decisiveness probability
def compute_decisiveness_probability(tree, taxa_sets, posterior):
    decisive_count = sum(is_decisive(taxa_sets, [tree]) for prob, tree in posterior)
    return decisive_count / len(posterior)

# Example usage with sequence alignment
tree, decisive_prob = perform_bayesian_inference(alignment, taxa_sets)
print(f"Posterior Decisiveness Probability: {decisive_prob:.4f}")
```

**Value**: Bayesian inference allows for a more nuanced, probabilistic analysis of tree decisiveness by integrating uncertainty in the tree topologies into the decisiveness assessment, offering deeper insights into how likely a given tree resolves taxa relationships.

---

### 4. **Decisiveness Across Different Evolutionary Models**
This example evaluates the decisiveness of phylogenetic trees constructed using different evolutionary models (e.g., Jukes-Cantor, Kimura) to see how the choice of model influences decisiveness.

```python
from Bio.Phylo.TreeConstruction import DistanceCalculator

# Evaluate decisiveness across different evolutionary models
models = ['identity', 'jukes-cantor', 'kimura']
decisive_results = {}

for model in models:
    calculator = DistanceCalculator(model)
    tree = constructor.build_tree(alignment, calculator=calculator)
    decisive_results[model] = is_decisive(taxa_sets, [tree])

# Display results
for model, decisive in decisive_results.items():
    print(f"Model: {model}, Decisive: {'Yes' if decisive else 'No'}")
```

**Value**: This example enriches phylogenetic analysis by exploring how different evolutionary models affect the decisiveness of the resulting trees, providing a robust and comparative approach to model selection in phylogenetics.

---

### 5. **Decisiveness-Based Pruning with Dynamic Tree Rearrangement**
This example combines dynamic tree rearrangement with decisiveness-based pruning, ensuring that phylogenetic trees retain only the informative branches while being dynamically rearranged for improved resolution.

```python
from Bio.Phylo.BaseTree import Clade

# Prune and rearrange tree based on decisiveness
def rearrange_and_prune_tree(tree, taxa_sets):
    pruned_tree = prune_non_informative(tree, taxa_sets)
    
    # Dynamic rearrangement: Rearrange clades to maximize decisiveness
    for clade in pruned_tree.find_clades(order="postorder"):
        if not is_decisive([clade.name], [pruned_tree]):
            pruned_tree.collapse(clade)
    
    return pruned_tree

# Example usage
rearranged_tree = rearrange_and_prune_tree(initial_tree, taxa_sets)
Phylo.draw(rearranged_tree)
```

**Value**: This example offers a dynamic and adaptive solution for improving tree clarity, where the tree structure is rearranged and pruned based on decisiveness, resulting in trees that are more informative and easier to interpret.

---

### **Smart File Name Suggestion**
`PhyloDecisiveness_Bayesian_Annealing_Diversity_ModelPrune.py`

This file name reflects the advanced complementary approaches, including Bayesian inference, simulated annealing, diversity assessment, and model comparison, along with pruning and rearrangement strategies for enhanced phylogenetic decisiveness.

---

These five additional examples complement the original set by delving into more sophisticated computational techniques, probabilistic analysis, and model comparisons. They provide robust, data-driven strategies to assess and optimize phylogenetic decisiveness, giving a richer understanding of phylogenetic tree dynamics and evolutionary relationships.
