```java
package com.colordash.game;

public class Character {

    private int positionX;
    private int positionY;
    private boolean isJumping;
    private boolean isSliding;

    public Character(int positionX, int positionY) {
        this.positionX = positionX;
        this.positionY = positionY;
        this.isJumping = false;
        this.isSliding = false;
    }

    public int getPositionX() {
        return positionX;
    }

    public void setPositionX(int positionX) {
        this.positionX = positionX;
    }

    public int getPositionY() {
        return positionY;
    }

    public void setPositionY(int positionY) {
        this.positionY = positionY;
    }

    public boolean isJumping() {
        return isJumping;
    }

    public void setJumping(boolean jumping) {
        isJumping = jumping;
    }

    public boolean isSliding() {
        return isSliding;
    }

    public void setSliding(boolean sliding) {
        isSliding = sliding;
    }

    public void jump() {
        if (!isJumping) {
            isJumping = true;
            // Logic for jumping
        }
    }

    public void slide() {
        if (!isSliding) {
            isSliding = true;
            // Logic for sliding
        }
    }

    public void moveForward() {
        // Logic for moving forward
    }
}
```