import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class SimpleSwingApp {
    public static void main() {
        // Erstelle das Hauptfenster
        JFrame frame = new JFrame("Einfaches Swing Programm");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 300);

        // Erstelle ein Panel zur Organisation der Komponenten
        JPanel panel = new JPanel();

        // Erstelle zwei Textfelder
        JTextField inputField1 = new JTextField(10);
        JTextField inputField2 = new JTextField(10);

        // Erstelle eine Liste mit Namen
        String[] names = {"Alice", "Bob", "Charlie", "Diana", "Horst", "Bernd", "Tarzan", "Sascha"};
        JList<String> nameList = new JList<>(names);
        nameList.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
        JScrollPane listScroller = new JScrollPane(nameList);
        listScroller.setPreferredSize(new java.awt.Dimension(100, 80));

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

        // Füge die Komponenten dem Panel hinzu
        panel.add(new JLabel("Eingabe 1:"));
        panel.add(inputField1);
        panel.add(new JLabel("Eingabe 2:"));
        panel.add(inputField2);
        panel.add(appendButton);
        panel.add(new JLabel("Namen:"));
        panel.add(listScroller);
        panel.add(showNameButton);

        // Füge das Panel dem Frame hinzu
        frame.add(panel);

        // Zeige das Fenster
        frame.setVisible(true);
    }
}
