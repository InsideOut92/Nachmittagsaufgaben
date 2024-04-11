package Klassen;

public class Hiding {
    private int KidsId;
    private int presentId;
    private String description;

    public Hiding() {
    }

    public Hiding(int kidsId, int presentId, String description) {
        KidsId = kidsId;
        this.presentId = presentId;
        this.description = description;
    }

    public int getKidsId() {
        return KidsId;
    }

    public void setKidsId(int kidsId) {
        KidsId = kidsId;
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

    @Override
    public String toString() {
        return "Hiding{" +
                "KidsId=" + KidsId +
                ", presentId=" + presentId +
                ", description='" + description + '\'' +
                '}';
    }
}
