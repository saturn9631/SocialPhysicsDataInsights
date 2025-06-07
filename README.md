# Social Physics Data Insights (formally PoliDataRectifier)
## Summary
In modern times there is a firehose of information and politics is no different, so this project was made to parse down all the data into a usable format. In this is a project to analyze politics using data and math borrowed from physics, economics and other places; all of which can be used to analyze everything from power structures, to relationship markets, to the shifting of opinions of a population. The main behind this project is combining symbolic math with machine learning to allow better and faster solution to the problem as well as better understanding of how the solution was generated.
## Math
Most of the math used in this application will be calculus, linear algebra, statistics, and game theory however more advanced math is planned: group theory, differential geometry, and functional analysis as well as some other miscellaneous stuff. The math will be discovered/verified using machine learning methods such as SINDy (Sparse Identification of Nonlinear Dynamics) and physics informed neural networks (which was the inspiration to take the application in this direction). One of the main goals of the application is to produce differential equations that predicts the decisions made by the entities (people, groups, organizations) based off of their payoffs, which will be called their strategy. The strategy and the associated DE can be shown along with the data to give insights as to what the entities are doing, why they are doining it, and what they will do in the future.
## Necessary Packages
### Python
1. numpy
2. pandas
3. scipy
4. sympy
6. networkx
7. torch (cuda/rocm)
    1. torchaudio
    2. torchvision
8. transformers (torch version) by huggingface
9. matplotlib
10. jupyter
### DataBase
As of now the only database is MySql, however any sql relational database would probably work. At a certain point a vector database and a search engine might be useful.
## Commit Rules
As of now there is not many since it is a small project, but code is welcome and so is math; the latter just needs to be in an issue or in a pull request to modify documentation.
### Sources
- [Steven Brunton's Playlist on Physics Informed Machine Learning](https://www.youtube.com/playlist?list=PLMrJAkhIeNNQ0BaKuBKY43k4xMo6NSbBa)
