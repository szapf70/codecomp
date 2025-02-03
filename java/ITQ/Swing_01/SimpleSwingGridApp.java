import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class SimpleSwingGridApp {
    public static void main() {
        // Erstelle das Hauptfenster
        JFrame frame = new JFrame("Einfaches Swing Programm");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(500, 300);

        // Erstelle ein Panel mit GridBagLayout
        JPanel panel = new JPanel(new GridBagLayout());
        GridBagConstraints gbc = new GridBagConstraints();

        // Erstelle zwei Textfelder
        JTextField inputField1 = new JTextField(10);
        JTextField inputField2 = new JTextField(10);

        // Erstelle eine Liste mit Namen
        String[] names = {"Alice", "Bob", "Charlie", "Diana","Alice", "Bob", "Charlie", "Diana"};
        JList<String> nameList = new JList<>(names);
        nameList.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
        JScrollPane listScroller = new JScrollPane(nameList);
        listScroller.setPreferredSize(new Dimension(100, 80));

        // Erstelle zwei Knöpfe
        JButton appendButton = new JButton("Erweitern und Kopieren");
        JButton showNameButton = new JButton("Zeige Name");

        // Füge Action Listener zum "Erweitern und Kopieren"-Knopf hinzu
        appendButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String text1 = inputField1.getText();
                // Hier erweitern wir den Text und kopieren ihn ins zweite Feld
                String expandedText = text1 + " - erweitert";
                inputField2.setText(expandedText);
            }
        });

        // Füge Action Listener zum "Zeige Name"-Knopf hinzu
        showNameButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String selectedName = nameList.getSelectedValue();
                if (selectedName != null) {
                    JOptionPane.showMessageDialog(frame, "Ausgewählter Name: " + selectedName);
                } else {
                    JOptionPane.showMessageDialog(frame, "Kein Name ausgewählt!");
                }
            }
        });

        // Hinzufügen der Komponenten zum Panel mit GridBagConstraints

        // Eingabe 1 Label
        gbc.gridx = 0;
        gbc.gridy = 0;
        gbc.anchor = GridBagConstraints.WEST;
        panel.add(new JLabel("Eingabe 1:"), gbc);

        // Eingabe 1 Textfeld
        gbc.gridx = 1;
        gbc.gridy = 0;
        panel.add(inputField1, gbc);

        // Eingabe 2 Label
        gbc.gridx = 0;
        gbc.gridy = 1;
        panel.add(new JLabel("Eingabe 2:"), gbc);

        // Eingabe 2 Textfeld
        gbc.gridx = 1;
        gbc.gridy = 1;
        panel.add(inputField2, gbc);

        // Erweitern und Kopieren Button
        gbc.gridx = 0;
        gbc.gridy = 4;
        gbc.gridwidth = 1;
        gbc.fill = GridBagConstraints.HORIZONTAL;
        panel.add(appendButton, gbc);

        // Namen Label
        gbc.gridx = 0;
        gbc.gridy = 3;
        gbc.gridwidth = 1;
        gbc.fill = GridBagConstraints.NONE;
        panel.add(new JLabel("Namen:"), gbc);

        // Namen Liste
        gbc.gridx = 1;
        gbc.gridy = 3;
        panel.add(listScroller, gbc);

        // Zeige Name Button
        gbc.gridx = 3;
        gbc.gridy = 4;
        gbc.gridwidth = 1;
        gbc.fill = GridBagConstraints.HORIZONTAL;
        panel.add(showNameButton, gbc);

        // Füge das Panel dem Frame hinzu
        frame.add(panel);

        // Zeige das Fenster
        frame.setVisible(true);
    }
}
