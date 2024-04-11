package Klassen;

public class Address {
    private int id;
    private String street;
    private String hnr;
    private String plz;
    private String city;
    private String country;

    public Address() {
    }

    public Address(String street, String hnr, String plz, String city, String country) {
        this.street = street;
        this.hnr = hnr;
        this.plz = plz;
        this.city = city;
        this.country = country;
    }

    public Address(int id, String street, String hnr, String plz, String city, String country) {
        this.id = id;
        this.street = street;
        this.hnr = hnr;
        this.plz = plz;
        this.city = city;
        this.country = country;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
    }

    public String getHnr() {
        return hnr;
    }

    public void setHnr(String hnr) {
        this.hnr = hnr;
    }

    public String getPlz() {
        return plz;
    }

    public void setPlz(String plz) {
        this.plz = plz;
    }

    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }

    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }

    public String toString(){
        return "Adresse{" +
                "ID= " + id +
                ", Street= " + street +
                ", HNR= " + hnr +
                ", PLZ= " + plz +
                ", City= " + city +
                ", Country= " + country + "}";
    }
}
