```java
package com.colordash.game;

import java.awt.Color;
import java.awt.Graphics2D;
import java.awt.Rectangle;

public class Gem {

    private int x, y;
    private Color color;
    private boolean collected;

    public Gem(int x, int y, Color color) {
        this.x = x;
        this.y = y;
        this.color = color;
        this.collected = false;
    }

    public void draw(Graphics2D g) {
        if (!collected) {
            g.setColor(color);
            g.fillOval(x, y, 10, 10);
        }
    }

    public void collect() {
        this.collected = true;
    }

    public boolean isCollected() {
        return collected;
    }

    public Rectangle getBounds() {
        return new Rectangle(x, y, 10, 10);
    }
}
```