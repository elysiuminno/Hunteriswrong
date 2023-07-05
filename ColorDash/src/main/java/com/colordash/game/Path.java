```java
package com.colordash.game;

import java.util.ArrayList;
import java.util.List;

public class Path {
    private List<Obstacle> obstacles;
    private List<Gem> gems;
    private int speed;

    public Path() {
        this.obstacles = new ArrayList<>();
        this.gems = new ArrayList<>();
        this.speed = 1;
    }

    public void scroll() {
        // Logic to scroll the path from right to left
        // This could involve moving the obstacles and gems in the opposite direction of the character's movement
    }

    public void increaseSpeed() {
        // Logic to increase the speed of the scrolling path as the game progresses
        this.speed++;
    }

    public void addObstacle(Obstacle obstacle) {
        this.obstacles.add(obstacle);
    }

    public void addGem(Gem gem) {
        this.gems.add(gem);
    }

    public List<Obstacle> getObstacles() {
        return obstacles;
    }

    public List<Gem> getGems() {
        return gems;
    }

    public int getSpeed() {
        return speed;
    }
}
```