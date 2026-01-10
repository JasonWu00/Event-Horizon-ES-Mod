# Components

This folder contains data files on components, in-game items that can be placed in a ship.   
Each component is made of two files: a component file and a stats file.   
Each pair of folders (`[faction name]` and `[faction name] Stats`) contains the component and stat file for a collection of components assigned to the named faction.

Below is an example of a component file, followed by a description of what each data field does.

```json
{
  "ItemType": 1,
  "Id": 9004,
  "Name": "Boxwing",
  "DisplayCategory": 5,
  "Availability": 2,
  "ComponentStatsId": 9004,
  "Faction": 203,
  "Level": 25,
  "Icon": "boxwing icon.png",
  "Layout": "111111111",
  "CellType": "1",
  "DroneBayId": 9004,
  "DroneId": 9004,
  "PossibleModifications": [
    17,
    18,
    19,
    20,
    2
  ]
}
```

Data fields:
- `"ItemType"`: Tells the database editor program what type of data file is being read (in this case: a component file).
- `"Id"`: Unique ID assigned to this file. Each component file must have a unique ID.
- `"Name"`: Name of the component as displayed in-game.
- `"DisplayCategory"`: Number denoting which category the game should display the component in.
  - Event Horizon sorts components into several categories (weapons, energy generation, armor and shields, drones, engines, special components).
- `"Availability"`: Number denoting the places that this component can appear in in-game.
- `"ComponentStatsID"`: Unique ID of the file containing the stats for this component.
- `"Faction"`: Unique ID of the faction the component belongs to. This field can be deleted for components not assigned to any faction.
- `"Level"`: A number that controls a variety of component traits (crafting costs, likelihood to appear in smuggler shops, etc).
- `"Icon"`: Image representing the component as displayed in-game.
- `"Layout"`: A string denoting the number of cells the component takes up in-game.
  - Every ship in Event Horizon contains a number of cells that can be occupied by components.
  - The string represents a two-dimensional grid of cells with its rows stacked end to end.
  - Every number in the string denotes an empty cell or an occupied cell.
- `"CellType"`: A string denoting the type of cell the component can occupy.
  - Event Horizon allows ships to display a variety of cells and components to occupy any one of them.
- `"DroneBayId"`: Unique ID of Drone Bay ID linked to this file.
  - Remove this field if the component is not meant to be a drone bay.
- `"DroneId"`: Unique ID of the ship build to be spawned by this component.
  - Remove this field if the component is not meant to be a drone bay.
- `"PossibleModifications"`: A list of modification IDs this component can receive when generated in-game.