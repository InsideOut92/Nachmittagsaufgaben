package Klassen;

public class Presents {
    private int presentId;
    private String description;
    private String color;

    public Presents() {
    }

    public Presents(String description, String color) {
        this.description = description;
        this.color = color;
    }

    public Presents(int presentId, String description, String color) {
        this.presentId = presentId;
        this.description = description;
        this.color = color;
    }

    public int getPresentId() {
        return presentId;
    }

    public void setPresentId(int presentId) {
        this.presentId = presentId;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    @Override
    public String toString() {
        return "Presents{" +
                "presentId=" + presentId +
                ", description='" + description + '\'' +
                ", color='" + color + '\'' +
                '}';
    }
}
