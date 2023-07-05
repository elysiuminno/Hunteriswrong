# Color Dash

Color Dash is a vibrant, visually appealing game where players control a small character that runs along a colorful path. The objective of the game is to navigate through the path while avoiding obstacles and collecting as many colored gems as possible.

## How it works

- The game features a path that continuously scrolls horizontally from right to left.
- The player's character automatically moves forward, and the player's task is to control the character's jumps and slides to avoid obstacles.
- Obstacles can include barriers, moving platforms, or even gaps in the path that require precise timing to cross.
- Along the path, there are colorful gems scattered at various heights. The player can collect these gems by jumping at the right time to reach them.
- Each collected gem adds to the player's score, and the goal is to achieve the highest score possible.
- As the game progresses, the speed of the scrolling path increases, making it more challenging to time the jumps and slides accurately.
- The game could include power-ups or special gems that provide temporary benefits, such as slowing down time or granting invincibility.

## Gameplay

The addictive nature of "Color Dash" lies in its simple yet engaging gameplay mechanics. Players can aim to beat their high scores or challenge friends to see who can collect the most gems and navigate the path for the longest distance. The colorful visuals and fast-paced nature of the game create a sense of excitement and keep players coming back for more attempts.

## Platform

Since "Color Dash" is self-contained and doesn't rely on external APIs or resources, it can be easily played on various platforms, including mobile devices, web browsers, or even as a standalone desktop game.

## Files

The project is structured as follows:

- `ColorDashApplication.java`: The main application file.
- `Character.java`: Defines the player's character.
- `Path.java`: Controls the scrolling path.
- `Obstacle.java`: Generates and controls the obstacles.
- `Gem.java`: Generates and controls the gems.
- `PowerUp.java`: Generates and controls the power-ups.
- `Score.java`: Keeps track of the player's score.
- `GameController.java`: Controls the game's logic.
- `GameView.java`: Controls the game's visuals.
- `application.properties`: Configures the application's settings.
- `pom.xml`: Manages the project's dependencies.

## Running the game

To run the game, navigate to the project's root directory and run the following command:

```bash
java -jar target/ColorDash-0.0.1-SNAPSHOT.jar
```

Please ensure to check your work multiple times to make sure it can run as is with no issue.