import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;

public class SimpleDrawing extends JFrame {
    
    private DrawingPanel drawingPanel;
    
    public SimpleDrawing() {
        setTitle("Simple Drawing");
        setSize(400, 400);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        drawingPanel = new DrawingPanel();
        add(drawingPanel, BorderLayout.CENTER);
        
        JButton saveButton = new JButton("Save as Image");
        saveButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                saveImage();
            }
        });
        add(saveButton, BorderLayout.SOUTH);
    }
    
    private void saveImage() {
        BufferedImage image = new BufferedImage(drawingPanel.getWidth(), drawingPanel.getHeight(), BufferedImage.TYPE_INT_RGB);
        Graphics2D g2 = image.createGraphics();
        drawingPanel.paint(g2);
        g2.dispose();
        
        try {
            ImageIO.write(image, "png", new File("drawing.png"));
            JOptionPane.showMessageDialog(this, "Image saved as drawing.png");
        } catch (IOException ex) {
            ex.printStackTrace();
            JOptionPane.showMessageDialog(this, "Error saving image.");
        }
    }
    
    private class DrawingPanel extends JPanel {
        @Override
        protected void paintComponent(Graphics g) {
            super.paintComponent(g);
            g.drawLine(50, 50, 200, 200);
            g.drawLine(200, 50, 50, 200);
            g.drawString("Hello, World!", 100, 150);
        }
    }
    
    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new SimpleDrawing().setVisible(true);
            }
        });
    }
}
