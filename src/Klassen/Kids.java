package Klassen;

import java.util.Date;

public class Kids {
    private int kidsId;
    private String firstname;
    private String lastname;
    private Date birthday;
    private int address;

    public Kids() {
    }

    public Kids(String firstname, String lastname, Date birthday, int address) {
        this.firstname = firstname;
        this.lastname = lastname;
        this.birthday = birthday;
        this.address = address;
    }

    public Kids(int kidsId, String firstname, String lastname, Date birthday, int address) {
        this.kidsId = kidsId;
        this.firstname = firstname;
        this.lastname = lastname;
        this.birthday = birthday;
        this.address = address;
    }

    public int getKidsId() {
        return kidsId;
    }

    public void setKidsId(int kidsId) {
        this.kidsId = kidsId;
    }

    public String getFirstname() {
        return firstname;
    }

    public void setFirstname(String firstname) {
        this.firstname = firstname;
    }

    public String getLastname() {
        return lastname;
    }

    public void setLastname(String lastname) {
        this.lastname = lastname;
    }

    public Date getBirthday() {
        return birthday;
    }

    public void setBirthday(Date birthday) {
        this.birthday = birthday;
    }

    public int getAddress() {
        return address;
    }

    public void setAddress(int address) {
        this.address = address;
    }

    @Override
    public String toString() {
        return "Kids{" +
                "kidsId=" + kidsId +
                ", firstname='" + firstname +
                ", lastname='" + lastname +
                ", birthday=" + birthday +
                ", address=" + address +
                '}';
    }
}
