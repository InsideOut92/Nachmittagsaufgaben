package GUI;

import GUI.Eingabe.Adresseingabe;
import Klassen.Address;
import SQL.SearchStmt;
import SQL.SelectStmt;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;

public class AddressFrame {
    JFrame frame = new JFrame("AdressVerwaltung");
    JPanel tablePanel = new JPanel();
    JScrollPane scrollPane = new JScrollPane(tablePanel,
            ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS,
            ScrollPaneConstants.HORIZONTAL_SCROLLBAR_NEVER);
    JButton backButton = new JButton("Zurück");
    JButton saveExitButton = new JButton("Speichern & Zurück");
    JButton createButton = new JButton("Erstellen");

    JLabel searchLabel = new JLabel("Suche: ");
    JTextField searchTF = new JTextField();

    ArrayList<Address> addresses = new ArrayList<>();


    BoxLayout tableBox = new BoxLayout(tablePanel, BoxLayout.Y_AXIS);

    JPanel panel = new JPanel();

    GridBagConstraints gbc = new GridBagConstraints();
    GridBagLayout gbl = new GridBagLayout();

    public AddressFrame(){}

    private void createAddressFrame(){
        panel.setLayout(gbl);
        gbl.setConstraints(panel, gbc);

        tablePanel.setLayout(tableBox);

        scrollPane.setPreferredSize(new Dimension(600, 500));
        gbc.gridy = 0;
        gbc.gridx = 0;
        gbc.gridwidth = 6;
        gbc.gridheight = 10;
        panel.add(scrollPane, gbc);

        gbc.gridy = 10;
        gbc.gridx = 0;
        gbc.gridheight = 1;
        gbc.gridwidth = 2;
        panel.add(createButton, gbc);

        gbc.gridx = 3;
        panel.add(backButton, gbc);

        gbc.gridx = 5;
        panel.add(saveExitButton, gbc);

        gbc.gridx = 0;
        gbc.gridy = 12;
        panel.add(searchLabel, gbc);

        searchTF.setPreferredSize(new Dimension(70, 20));
        gbc.gridx = 3;
        panel.add(searchTF, gbc);

        updateAddresses();


        frame.add(panel);
        frame.setSize(900, 700);
        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        frame.setVisible(true);
    }

    public void main(){
        javax.swing.SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                createAddressFrame();
                setButtonListener();
            }
        });
    }

    private void setButtonListener(){
        ActionListener createListener = new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                Adresseingabe adresseingabe = new Adresseingabe();
                adresseingabe.main();
                updateAddresses();
            }
        };
        createButton.addActionListener(createListener);

        ActionListener enterListener = new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                updateAddresses();
            }
        };
        searchTF.addActionListener(enterListener);
    }

    private void updateAddresses(){
        String searchText = searchTF.getText();
        if (searchText.isEmpty()){
            System.out.println("Searchtext: " + searchText);
            addresses = SelectStmt.findAllAddresses();
        } else {
            System.out.println("Searching: " + searchText);
            addresses = SearchStmt.searchAllAddresses(searchText);
        }
        tablePanel.removeAll();


        for(int i = 0; i < addresses.size(); i++){
            AddressPanel aPanel = new AddressPanel(addresses.get(i));
            tablePanel.add(aPanel);
        }
        tablePanel.revalidate();
        tablePanel.repaint();
        scrollPane.revalidate();
        scrollPane.repaint();
    }




}
