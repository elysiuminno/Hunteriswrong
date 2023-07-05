```java
package com.colordash.game;

public class Score {
    private int score;

    public Score() {
        this.score = 0;
    }

    public int getScore() {
        return this.score;
    }

    public void increaseScore(int value) {
        this.score += value;
    }

    public void resetScore() {
        this.score = 0;
    }
}
```