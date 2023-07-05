```java
package com.colordash.game;

import javax.swing.*;
import java.awt.*;

public class GameView extends JPanel {

    private Character character;
    private Path path;
    private Obstacle obstacle;
    private Gem gem;
    private PowerUp powerUp;
    private Score score;

    public GameView(Character character, Path path, Obstacle obstacle, Gem gem, PowerUp powerUp, Score score) {
        this.character = character;
        this.path = path;
        this.obstacle = obstacle;
        this.gem = gem;
        this.powerUp = powerUp;
        this.score = score;
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        drawPath(g);
        drawCharacter(g);
        drawObstacle(g);
        drawGem(g);
        drawPowerUp(g);
        drawScore(g);
    }

    private void drawPath(Graphics g) {
        // Draw the path
    }

    private void drawCharacter(Graphics g) {
        // Draw the character
    }

    private void drawObstacle(Graphics g) {
        // Draw the obstacle
    }

    private void drawGem(Graphics g) {
        // Draw the gem
    }

    private void drawPowerUp(Graphics g) {
        // Draw the power-up
    }

    private void drawScore(Graphics g) {
        // Draw the score
    }
}
```