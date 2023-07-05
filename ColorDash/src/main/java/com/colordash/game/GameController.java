```java
package com.colordash.game;

import java.util.ArrayList;
import java.util.List;

public class GameController {

    private Character character;
    private Path path;
    private List<Obstacle> obstacles;
    private List<Gem> gems;
    private List<PowerUp> powerUps;
    private Score score;

    public GameController() {
        this.character = new Character();
        this.path = new Path();
        this.obstacles = new ArrayList<>();
        this.gems = new ArrayList<>();
        this.powerUps = new ArrayList<>();
        this.score = new Score();
    }

    public void startGame() {
        this.character.startMoving();
        this.path.startScrolling();
    }

    public void pauseGame() {
        this.character.stopMoving();
        this.path.stopScrolling();
    }

    public void resumeGame() {
        this.character.startMoving();
        this.path.startScrolling();
    }

    public void endGame() {
        this.character.stopMoving();
        this.path.stopScrolling();
        this.score.reset();
    }

    public void moveCharacter() {
        this.character.move();
    }

    public void generateObstacle() {
        Obstacle obstacle = new Obstacle();
        this.obstacles.add(obstacle);
    }

    public void collectGem() {
        for (Gem gem : gems) {
            if (character.isCollidingWith(gem)) {
                this.score.increment();
                gems.remove(gem);
                break;
            }
        }
    }

    public void activatePowerUp() {
        for (PowerUp powerUp : powerUps) {
            if (character.isCollidingWith(powerUp)) {
                powerUp.activate();
                powerUps.remove(powerUp);
                break;
            }
        }
    }

    public void updateScore() {
        this.score.update();
    }
}
```