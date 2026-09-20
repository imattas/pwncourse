# Writeup: tcache-reuse

The allocator returns the same address for the same-size allocation after free in the common local configuration. That observation is version-sensitive and must be verified rather than assumed. A tcache-poisoning chain would require a write primitive against freed metadata and a valid target; this fixture intentionally stops before that step.

