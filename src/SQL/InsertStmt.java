package SQL;

import DatabaseOperations.DB;
import Klassen.*;
import Umwandlungen.Umwandlung;

import java.sql.SQLException;
import java.sql.Statement;

public class InsertStmt {

    public static int addAddress(Address address){
        String query = "INSERT INTO address (street, hnr, plz, city, country) " +
                "VALUES (?,?,?,?,?)";
        try(
                var conn = DB.userconnect();
                var pstmt = conn.prepareStatement(query, Statement.RETURN_GENERATED_KEYS)
        ){
            pstmt.setString(1, address.getStreet());
            pstmt.setString(2, address.getHnr());
            pstmt.setString(3, address.getPlz());
            pstmt.setString(4, address.getCity());
            pstmt.setString(5, address.getCountry());

            int insertedRows = pstmt.executeUpdate();
            if(insertedRows > 0){
                var rs = pstmt.getGeneratedKeys();
                if(rs.next()){
                    return rs.getInt(1);
                }
            }
        } catch (SQLException e){
            e.printStackTrace();
        }
        return -1;
    }

    public static int addKids(Kids kid){
        String query = "INSERT INTO Kids (firstname, lastname, birthday, address) " +
                "VALUES (?,?,?,?)";
        try(
                var conn = DB.userconnect();
                var pstmt = conn.prepareStatement(query, Statement.RETURN_GENERATED_KEYS)
        ){
            pstmt.setString(1, kid.getFirstname());
            pstmt.setString(2, kid.getLastname());
            pstmt.setDate(3, Umwandlung.dateUmwandlung(kid.getBirthday()));
            pstmt.setInt(4, kid.getAddress());

            int insertedRows = pstmt.executeUpdate();
            if(insertedRows > 0){
                var rs = pstmt.getGeneratedKeys();
                if(rs.next()){
                    return rs.getInt(1);
                }
            }
        } catch (SQLException e){
            e.printStackTrace();
        }
        return -1;
    }

    public static int addPresent(Presents present){
        String query = "INSERT INTO Presents (description, color) " +
                "VALUES (?,?)";
        try(
                var conn = DB.userconnect();
                var pstmt = conn.prepareStatement(query, Statement.RETURN_GENERATED_KEYS)
        ){
            pstmt.setString(1, present.getDescription());
            pstmt.setString(2, present.getColor());

            int insertedRows = pstmt.executeUpdate();
            if(insertedRows > 0){
                var rs = pstmt.getGeneratedKeys();
                if(rs.next()){
                    return rs.getInt(1);
                }
            }
        } catch (SQLException e){
            e.printStackTrace();
        }
        return -1;
    }

    public static int addHiding(Hiding hiding){
        String query = "INSERT INTO Hiding (kidsId, presentId, description) " +
                "VALUES (?,?,?)";
        try(
                var conn = DB.userconnect();
                var pstmt = conn.prepareStatement(query, Statement.RETURN_GENERATED_KEYS)
        ){
            pstmt.setInt(1, hiding.getKidsId());
            pstmt.setInt(2, hiding.getPresentId());
            pstmt.setString(3, hiding.getDescription());

            int insertedRows = pstmt.executeUpdate();
            if(insertedRows > 0){
                var rs = pstmt.getGeneratedKeys();
                if(rs.next()){
                    return rs.getInt(1);
                }
            }
        } catch (SQLException e){
            e.printStackTrace();
        }
        return -1;
    }

    public static int addWishlist(Wishlist wishlist){
        String query = "INSERT INTO Kids (kidsId, presentId, year) " +
                "VALUES (?,?,?)";
        try(
                var conn = DB.userconnect();
                var pstmt = conn.prepareStatement(query, Statement.RETURN_GENERATED_KEYS)
        ){
            pstmt.setInt(1, wishlist.getKindId());
            pstmt.setInt(2, wishlist.getPresentId());
            pstmt.setInt(3, wishlist.getYear());

            int insertedRows = pstmt.executeUpdate();
            if(insertedRows > 0){
                var rs = pstmt.getGeneratedKeys();
                if(rs.next()){
                    return rs.getInt(1);
                }
            }
        } catch (SQLException e){
            e.printStackTrace();
        }
        return -1;
    }

    public static void main(String[] args) {
        Address address = new Address("Kieler Hafen", "9", "08152", "Kiel", "Deutschland");
        addAddress(address);
    }
}
