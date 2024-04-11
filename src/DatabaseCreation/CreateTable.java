package DatabaseCreation;

import DatabaseOperations.DB;

import java.sql.Connection;
import java.sql.SQLException;
import java.sql.Statement;

public class CreateTable {

    public static void createAll(){
        createAddress();
        createKids();
        createPresents();
        createWishlist();
        createHiding();
    }

    public static void createQuery(String query){
        try(
                Connection conn = DB.adminconnect();
                Statement stmt = conn.createStatement()
                ){
            stmt.executeUpdate(query);
        } catch (SQLException e){
            e.printStackTrace();
        }
    }

    public static void createAddress(){
        String query = "CREATE TABLE IF NOT EXISTS Address(" +
                "AddressID SERIAL PRIMARY KEY," +
                "Street VARCHAR(30) NOT NULL," +
                "HNR VARCHAR(5) NOT NULL," +
                "PLZ VARCHAR(5) NOT NULL," +
                "City VARCHAR(30) NOT NULL," +
                "Country VARCHAR(50) NOT NULL," +
                "CONSTRAINT uni_address " +
                    "UNIQUE (Street, HNR, PLZ, City, Country))";
        createQuery(query);
        System.out.println("Houses build");
    }

    public static void createKids(){
        String query = "CREATE TABLE IF NOT EXISTS Kids(" +
                "KidsID SERIAL PRIMARY KEY," +
                "Firstname VARCHAR(30) NOT NULL," +
                "Lastname VARCHAR(30) NOT NULL," +
                "Birthday DATE NOT NULL," +
                "AddressID INTEGER NOT NULL," +
                "CONSTRAINT uni_kid " +
                    "UNIQUE (Firstname, Lastname, Birthday, AddressID)," +
                "CONSTRAINT fk_address " +
                    "FOREIGN KEY (AddressID) " +
                        "REFERENCES Address(AddressID))";
        createQuery(query);
        System.out.println("Created Life");
    }

    public static void createPresents(){
        String query = "CREATE TABLE IF NOT EXISTS Presents(" +
                "PresentID SERIAL PRIMARY KEY," +
                "Description VARCHAR(30) NOT NULL," +
                "COLOR VARCHAR(30)," +
                "CONSTRAINT uni_desc " +
                    "UNIQUE (Description))";
        createQuery(query);
        System.out.println("Presents packed");
    }

    public static void createWishlist(){
        String query = "CREATE TABLE IF NOT EXISTS Wishlist(" +
                "KindID INTEGER NOT NULL," +
                "PresentID INTEGER NOT NULL," +
                "Year INTEGER NOT NULL," +
                "CONSTRAINT pk_wish " +
                    "PRIMARY KEY (KindID, PresentID, Year)," +
                "CONSTRAINT fk_kind " +
                    "FOREIGN KEY (KindID)" +
                        "REFERENCES Kids(KidsID)," +
                "CONSTRAINT fk_present " +
                    "FOREIGN KEY (PresentID)" +
                        "REFERENCES Presents(PresentID))";
        createQuery(query);
        System.out.println("Wishes wished");
    }

    public static void createHiding(){
        String query = "CREATE TABLE IF NOT EXISTS Hiding(" +
                "KindID INTEGER NOT NULL," +
                "PresentID INTEGER NOT NULL," +
                "Description VARCHAR(60) NOT NULL," +
                "CONSTRAINT pk_hiding " +
                    "PRIMARY KEY (KindID, PresentID, Description)," +
                "CONSTRAINT fk_kind " +
                    "FOREIGN KEY (KindID)" +
                        "REFERENCES Kids(KidsID)," +
                "CONSTRAINT fk_present " +
                    "FOREIGN KEY (PresentID)" +
                        "REFERENCES Presents (PresentID))";
        createQuery(query);
        System.out.println("Presents hidden");
    }

    public static void main(String[] args) {
        createAll();
    }
}
