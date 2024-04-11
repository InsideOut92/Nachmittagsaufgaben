package GUI.Eingabe;

import GUI.AddressFrame;
import Klassen.Address;
import SQL.InsertStmt;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Adresseingabe {
    JFrame frame = new JFrame("Adresseingabe");
    JLabel streetLabel = new JLabel("Straßenname: ");
    JTextField streetTF = new JTextField(null);
    JLabel hnrLabel = new JLabel("Hausnummer: ");
    JTextField hnrTF = new JTextField(null);
    JLabel plzLabel = new JLabel("Postleitzahl: ");
    JTextField plzTF = new JTextField(null);
    JLabel cityLabel = new JLabel("Ort: ");
    JTextField cityTF = new JTextField(null);
    JLabel countryLabel = new JLabel("Land: ");
    JTextField countryTF = new JTextField(null);

    JButton execute = new JButton("Ok");
    JButton abort = new JButton("Abbrechen");

    JPanel panel = new JPanel();
    GridBagLayout gbl = new GridBagLayout();
    GridBagConstraints gbc = new GridBagConstraints();
    AddressFrame addressFrame;

    public Adresseingabe(){ }

    public void createFrame(){
        panel.setLayout(gbl);
        gbl.setConstraints(panel, gbc);

        gbc.gridx = 0;
        gbc.gridy = 0;
        panel.add(streetLabel, gbc);

        streetTF.setPreferredSize(new Dimension(70, 20));
        gbc.gridx = 1;
        panel.add(streetTF, gbc);

        gbc.gridx = 0;
        gbc.gridy = 1;
        panel.add(hnrLabel, gbc);

        hnrTF.setPreferredSize(new Dimension(70, 20));
        gbc.gridx = 1;
        panel.add(hnrTF, gbc);

        gbc.gridx = 0;
        gbc.gridy = 2;
        panel.add(plzLabel, gbc);

        plzTF.setPreferredSize(new Dimension(70, 20));
        gbc.gridx = 1;
        panel.add(plzTF, gbc);

        gbc.gridx = 0;
        gbc.gridy = 3;
        panel.add(cityLabel, gbc);

        cityTF.setPreferredSize(new Dimension(70, 20));
        gbc.gridx = 1;
        panel.add(cityTF, gbc);

        gbc.gridx = 0;
        gbc.gridy = 4;
        panel.add(countryLabel, gbc);

        countryTF.setPreferredSize(new Dimension(70, 20));
        gbc.gridx = 1;
        panel.add(countryTF, gbc);

        gbc.gridx = 0;
        gbc.gridy = 6;
        panel.add(execute, gbc);

        gbc.gridx = 1;
        panel.add(abort, gbc);

        frame.add(panel);
        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);

        frame.setSize(120, 80);
        frame.setVisible(true);
    }

    public void main(){
        javax.swing.SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                createFrame();
                setButtonListener();
            }
        });
    }

    private void createAddress(){
        String street = streetTF.getText();
        String hnr = hnrTF.getText();
        String plz = plzTF.getText();
        String city = cityTF.getText();
        String country = countryTF.getText();

        Pattern hnrPattern = Pattern.compile("^[0-9]*( ?[a-z]?|[0-9]* ?[0-9]\\/[0-9])?$", Pattern.CASE_INSENSITIVE);
        Matcher hnrMatcher = hnrPattern.matcher(hnr);

        Pattern plzPattern = Pattern.compile("^[0-9]{4,5}$", Pattern.CASE_INSENSITIVE);
        Matcher plzMatcher = plzPattern.matcher(plz);

        if (street.isEmpty() || hnr.isEmpty() || plz.isEmpty() || city.isEmpty() || country.isEmpty()){
            // Langfristig durch PopUp ersetzen
            System.out.println("Nein, hier gibt es einen Fehler.");
        } else if (!(hnrMatcher.find() && plzMatcher.find() && hnr.length() < 6)) {
            // Langfristig durch PopUp ersetzen
            System.out.println("HNR oder PLZ entsprechen nicht den Erwartungen");
        } else {
            Address address = new Address(street, hnr, plz, city, country);
            InsertStmt.addAddress(address);
            frame.dispose();
        }
    }

    private void setButtonListener(){
        ActionListener executeListener = new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                createAddress();
            }
        };
        execute.addActionListener(executeListener);

        ActionListener abortListener = new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                frame.dispose();
            }
        };
        abort.addActionListener(abortListener);
    }


}
