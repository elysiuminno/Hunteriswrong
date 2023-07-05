```java
package com.colordash.game;

public class PowerUp {
    private String type;
    private boolean isActive;

    public PowerUp(String type) {
        this.type = type;
        this.isActive = false;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public boolean isActive() {
        return isActive;
    }

    public void setActive(boolean active) {
        isActive = active;
    }

    public void activatePowerUp() {
        this.isActive = true;
    }

    public void deactivatePowerUp() {
        this.isActive = false;
    }
}
```