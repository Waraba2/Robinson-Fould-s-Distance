from Bio import Phylo
from io import StringIO

# Read in the two trees in Newick format
tree1 = Phylo.read(StringIO("((A,B),C)"), "newick")
tree2 = Phylo.read(StringIO("((A,B),D)"), "newick")

# Initialize a counter for the number of splits that differ between the trees
split_differences = 0

# Iterate through each of the nodes in the first tree
for node in tree1.get_nonterminals():
  # Find the corresponding node in the second tree (if it exists)
  corresponding_node = tree2.find_any(node.name)

  # If the two nodes are not equivalent, increment the counter
  if corresponding_node is None or corresponding_node.clade != node.clades:
    split_differences += 1

# Return the Robinson Fould's distance between the two trees
print(split_differences)