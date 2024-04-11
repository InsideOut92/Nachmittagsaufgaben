package GUI;

import GUI.Eingabe.PresentEingabe;
import SQL.SelectStmt;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class PresentFrame {
    JFrame frame = new JFrame("PresentVerwaltung");
    JPanel tablePanel = new JPanel();
    JButton backButton = new JButton("Zurück");
    JButton saveExitButton = new JButton("Speichern & Zurück");
    JButton createButton = new JButton("Erstellen");

    BoxLayout tableBox = new BoxLayout(tablePanel, BoxLayout.Y_AXIS);

    public PresentFrame(){}

    private void createPresentFrame(){
        JPanel panel = new JPanel();

        GridBagConstraints gbc = new GridBagConstraints();
        GridBagLayout gbl = new GridBagLayout();

        panel.setLayout(gbl);
        gbl.setConstraints(panel, gbc);

        tablePanel.setLayout(tableBox);

        gbc.gridy = 0;
        gbc.gridx = 0;
        gbc.gridwidth = 6;
        gbc.gridheight = 10;
        panel.add(tablePanel, gbc);

        gbc.gridy = 10;
        gbc.gridx = 0;
        gbc.gridheight = 1;
        gbc.gridwidth = 2;
        panel.add(createButton, gbc);

        gbc.gridx = 3;
        panel.add(backButton, gbc);

        gbc.gridx = 5;
        panel.add(saveExitButton, gbc);

        var presentList = SelectStmt.findAllPresents();
        for(int i = 0; i < presentList.size(); i++){
            PresentPanel pPanel = new PresentPanel(presentList.get(i));
            tablePanel.add(pPanel);
        }

        frame.add(panel);
        frame.setSize(900, 700);
        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        frame.setVisible(true);
    }

    public void main(){
        javax.swing.SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                createPresentFrame();
                setButtonListener();
            }
        });
    }

    private void setButtonListener(){
        ActionListener createListener = new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                PresentEingabe presentEingabe = new PresentEingabe();
                presentEingabe.main();
            }
        };
        createButton.addActionListener(createListener);
    }
}
