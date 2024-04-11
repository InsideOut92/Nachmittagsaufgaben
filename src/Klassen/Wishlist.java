package Klassen;

public class Wishlist {
    private int kindId;
    private int presentId;
    private int year;

    public Wishlist() {
    }

    public Wishlist(int kindId, int presentId, int year) {
        this.kindId = kindId;
        this.presentId = presentId;
        this.year = year;
    }

    public int getKindId() {
        return kindId;
    }

    public void setKindId(int kindId) {
        this.kindId = kindId;
    }

    public int getPresentId() {
        return presentId;
    }

    public void setPresentId(int presentId) {
        this.presentId = presentId;
    }

    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }

    @Override
    public String toString() {
        return "Wishlist{" +
                "kindId=" + kindId +
                ", presentId=" + presentId +
                ", year=" + year +
                '}';
    }
}
