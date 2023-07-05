```java
package com.colordash.game;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class ColorDashApplication {

    public static void main(String[] args) {
        SpringApplication.run(ColorDashApplication.class, args);
    }

    private Character character;
    private Path path;
    private Obstacle obstacle;
    private Gem gem;
    private PowerUp powerUp;
    private Score score;
    private GameController gameController;
    private GameView gameView;

    public ColorDashApplication() {
        this.character = new Character();
        this.path = new Path();
        this.obstacle = new Obstacle();
        this.gem = new Gem();
        this.powerUp = new PowerUp();
        this.score = new Score();
        this.gameController = new GameController(character, path, obstacle, gem, powerUp, score);
        this.gameView = new GameView(gameController);
    }

    public void startGame() {
        gameController.startGame();
    }

    public void pauseGame() {
        gameController.pauseGame();
    }

    public void resumeGame() {
        gameController.resumeGame();
    }

    public void endGame() {
        gameController.endGame();
    }
}
```