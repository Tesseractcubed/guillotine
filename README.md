# guillotine
Headless graph based game tool, intended to help with parsing of diplomacy maps. Mainly focused on enabling better logic for storage, operations on content, and graphics rendering for graph based games.

This particular package uses test driven coding philosophy, mainly because the additional effort up front should solve issues that can occur as a codebase develops.

This builds on work in projects like DiploGM, and the softwares of Realpolitik, vDiplomacy, webDiplomacy, and others. Guillotine is intended to be robust, and potentially be expanded into a tool like Realpolitik, but the future is the future.

Brief design goals:
 - Create a storage format for configurations of graph based games, with the ability to hold attributes about both any node and any adjacency. This isn't necessarily a fixed configuration, but mostly a starting one.
 - Create a game data storage format, specifically for the non-configuration based details that change during the game. These may be able to be colocated with the configuration data, but would need to be separated somehow.
 - Create a graphical processing tool, including storing graphic data.. mostly locations to render image elements at.. creating an edited copy of a base graphic, and then publishing it to local files

Some initial design decisions are as follows:
 - Separate out configuration data, game data, and graphical data into three separate modules.
 - Support .svg graphical formats, mainly because direct editing of the XML before rendering is a benefit.
 - Program in Python, mainly due to good enough performance, useful packages, and experience with