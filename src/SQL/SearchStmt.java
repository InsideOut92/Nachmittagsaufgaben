package SQL;

import DatabaseOperations.DB;
import Klassen.Address;

import java.sql.SQLException;
import java.util.ArrayList;

public class SearchStmt {
    public static ArrayList<Address> searchAllAddresses(String searchText){
        var addresses = new ArrayList<Address>();

        var sql = "SELECT * FROM address WHERE " +
                "street LIKE '%" + searchText + "%' OR " +
                "hnr LIKE '%" + searchText + "%' OR " +
                "plz LIKE '%" + searchText + "%' OR " +
                "city LIKE '%" + searchText + "%' OR " +
                "country LIKE '%" + searchText + "%'";

        try(
                var conn = DB.userconnect();
                var stmt = conn.createStatement()
        ){
            var resultSet = stmt.executeQuery(sql);

            while(resultSet.next()){
                var address = new Address(
                        resultSet.getInt("addressid"),
                        resultSet.getString("street"),
                        resultSet.getString("hnr"),
                        resultSet.getString("plz"),
                        resultSet.getString("city"),
                        resultSet.getString("country")
                );
                addresses.add(address);
            }
        } catch (SQLException e){
            e.printStackTrace();
        }

        return addresses;
    }
}
