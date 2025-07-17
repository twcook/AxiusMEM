Refactor the code so that TRIPLESTORE_REPOSITORY isn't used, but a repository/dataset is passed as a requirement whereever needed.
This will allow for more flexibility and reuse. For example, for agent activity, the developer can pass 'agents' as the repository/dataset.
The connections made in AxiusMEM can then be resued in applications for other connectivity to the TRIPLESTORE. For example, passing, 'data', or other repositories can be used for general application use.
Actually, rethinking it. Leave the TRIPLESTORE_REPOSITORY as is, but make it a fallback if none is passed.









