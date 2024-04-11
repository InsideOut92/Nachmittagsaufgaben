package DatabaseCreation;

import DatabaseOperations.DB;

import java.sql.SQLException;

public class BulkInsert {

    public static void insertAll(){
        addAddresses();
        addKids();
        addPresents();
    }

    public static void addAddresses(){
        String query = "INSERT INTO address (street, hnr, plz, city, country) " +
                "VALUES " +
                "('Rostocker Straße', '21', '15236', 'Bärlin', 'Deutschland')," +
                "('Flensburg-Platz', '7 1/4', '65433', 'Frankfurt/Main', 'Deutschland')," +
                "('Martin-Luther-King-Alley', '9001', '76543', 'WA-Seattle', 'USA')";

        try(
                var conn = DB.adminconnect();
                var stmt = conn.createStatement()
        ){
            stmt.executeUpdate(query);
        } catch (SQLException e){
            e.printStackTrace();
        }
    }

    public static void addKids(){
        String query = "INSERT INTO Kids (firstname, lastname, birthday, addressId) " +
                "VALUES " +
                "('Anna', 'Meier', '2010-12-31', 1)," +
                "('Lena', 'Meier', '2011-12-31', 1)," +
                "('Lukas', 'Huber', '2020-02-20', 2)";

        try(
                var conn = DB.adminconnect();
                var stmt = conn.createStatement()
        ){
            stmt.executeUpdate(query);
        } catch (SQLException e){
            e.printStackTrace();
        }
    }

    public static void addPresents(){
        String query = "INSERT INTO Presents (description, color) " +
                "VALUES " +
                "('Nusslikör', NULL)," +
                "('Überraschungsei', 'Weiß')," +
                "('Schokohase', 'Braun')";

        try(
                var conn = DB.adminconnect();
                var stmt = conn.createStatement()
        ){
            stmt.executeUpdate(query);
        } catch (SQLException e){
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        insertAll();
    }
}
