package GUI;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.zip.GZIPInputStream;

public class OsterhasenGUI {
    JFrame frame = new JFrame("Osterhasen-Verwaltung");
    JButton addressButton = new JButton("Adress-Verwaltung");
    JButton kindButton = new JButton("Kinder-Veraltung");
    JButton hideButton = new JButton("Versteck-Verwaltung");
    JButton presentButton = new JButton("Geschenk-Verwaltung");
    JButton wishButton = new JButton("Wunschlisten-Verwaltung");

    public OsterhasenGUI(){}

    private void createAndShowGUI(){
        JPanel panel = new JPanel();

        GridBagLayout gbl = new GridBagLayout();
        GridBagConstraints gbc = new GridBagConstraints();
        panel.setLayout(gbl);
        gbl.setConstraints(panel, gbc);

        gbc.gridx = 0;
        gbc.gridy = 0;
        gbc.gridwidth = 4;
        panel.add(addressButton, gbc);

        gbc.gridy = 1;
        panel.add(kindButton, gbc);

        gbc.gridy = 2;
        panel.add(presentButton, gbc);

        gbc.gridy = 3;
        panel.add(hideButton, gbc);

        gbc.gridy = 4;
        panel.add(wishButton, gbc);

        frame.add(panel);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        frame.setSize(800, 600);
        frame.setVisible(true);
    }

    public void main(){
        javax.swing.SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                createAndShowGUI();
                setButtonListener();
            }
        });
    }

    private void setButtonListener(){
        ActionListener addressListener = new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                EventQueue.invokeLater(new Runnable() {
                    @Override
                    public void run() {
                        AddressFrame adressFrame = new AddressFrame();
                        adressFrame.main();
                    }
                });
            }
        };
        addressButton.addActionListener(addressListener);

        ActionListener presentListener = new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                EventQueue.invokeLater(new Runnable() {
                    @Override
                    public void run() {
                        PresentFrame presentFrame = new PresentFrame();
                        presentFrame.main();
                    }
                });
            }
        };
        presentButton.addActionListener(presentListener);
    }

}
