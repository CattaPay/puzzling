
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.HashMap;

public class Main {
    public static BoardArray runThing(Board board, Piece[] pieces){
        BoardArray boards = new BoardArray(board);
        for (Piece piece : pieces) {
            boards = boards.tryPiece(piece);
            System.out.println(boards.length());
        }
        // boards.printAll();
        return boards;
    }

    public static int dayAnswers(Piece[] pieces, int[][] dayBlockers) {
        int[][] blockers = {{6,3}, {6,4}, {6,5}, {6,6}, {0,6}, {1,6}, {-1,-1}, {-1,-1}};
        for (int i = 0; i < 2; i++) {
            blockers[i+6] = dayBlockers[i];
        }

        Board board = new Board(7, 7, blockers);
        BoardArray boards = new BoardArray(board);
        board.print();
        for (Piece piece : pieces) {
            boards = boards.tryPiece(piece);
            System.out.println(boards.length());
        }
        boards.printAll();
        return boards.length();
    }

    public static long dayBits(int[][] dayBlockers){
        long bits = 0;
        for (int i = 0; i < 8; i++){
            for (int j = 0; j < 8; j++){
                bits <<= 1;
                for (int k = 0; k < 2; k++) {
                    if (dayBlockers[k][0] == i & dayBlockers[k][1] == j){
                        bits++;
                    }
                }
            }
        }
        return bits;
    }

    public static void main(String[] args) throws IOException{

        int[][] coords = {{0, 0},
                          {0, 1},
                          {0, 2},
                          {1, 2},
                          {1, 3}};
        
        int[][] blockers = {{6,3}, {6,4}, {6,5}, {6,6}, {0,6}, {1,6}};
        int[][] blockers2 = {{6,3}, {6,4}, {6,5}, {6,6}, {0,6}, {1,6}};
        Board board = new Board(7,7,blockers2);


        int[][] rect = {{0,0}, {0,1}, {0,2}, {1,0}, {1,1}, {1,2}};
        int[][] angle = {{0,0}, {0,1}, {0,2}, {1,2}, {2,2}};
        int[][] zed = {{0,0}, {0,1}, {1,1}, {2,1}, {2,2}};
        int[][] yu = {{0,0}, {1,0}, {1,1}, {1,2}, {0,2}};
        int[][] l = {{0,0}, {0,1}, {0,2}, {0,3}, {1,0}};
        int[][] squiggle = {{0,0}, {0,1}, {1,1}, {1,2}, {1,3}};
        int[][] t = {{0,0}, {0,1}, {0,2}, {0,3}, {1,2}};
        int[][] nice = {{0,0}, {0,1}, {0,2}, {1,1}, {1,2}};
        // Piece piece = new Piece(coords, 'c');
        // piece.printGrid();
        // piece.getOrientations();
        // piece.printOrientations();

        // board.print();
        Piece rectanglePiece = new Piece(rect, 'G');
        Piece anglePiece = new Piece(angle, 'B');
        Piece zPiece = new Piece(zed, 'Z');
        Piece uPiece = new Piece(yu, 'U');
        Piece lPiece = new Piece(l, 'L');
        Piece squigglePiece = new Piece(squiggle, 'S');
        Piece tPiece = new Piece(t, 'T');
        Piece nicePiece = new Piece(nice, 'N');

        Piece[] pieces = {rectanglePiece, anglePiece, zPiece, uPiece, lPiece, squigglePiece, tPiece, nicePiece};
        
        // Board rawBoard = new Board(8, 8, new int[0][2]);
        BoardArray boards;
        
        boards = runThing(board, pieces);

        int[][] possibleBlockers = new int[43][2];
        Boolean flag;
        int count = 0;
        for (int i = 0; i < 7; i++){
            for (int j = 0; j < 7; j++){
                flag = Boolean.FALSE;
                for (int[] coord : blockers) {
                    if (i == coord[0] & j == coord[1]){
                        flag = Boolean.TRUE;
                    }
                }
                if (!flag){
                    possibleBlockers[count][0] = i;
                    possibleBlockers[count][1] = j;
                    count++;
                }
            }
        }

        int[][] newBlockers = {{2,5}, {3,4}};
        // dayAnswers(pieces, newBlockers);

        long boardHoles;
        long mesh;
        Board baseBoard = new Board(7,7,blockers);
        int[][] holes = new int[2][2];
        long bit;
        int k;
        String holesRep;

        HashMap<String, Integer> counters = new HashMap<String, Integer>();

        for (BoardPieces solved : boards.boards) {
            boardHoles = solved.findHoles(8);
            mesh = ~boardHoles & ~baseBoard.bitmap;
            // System.out.println(mesh);
            k = 0;
            for (int i = 0; i < 8; i++){
                for (int j = 0; j < 8; j++){
                    bit = (mesh >> (63 - (i * 8 + j))) & 1;
                    if (bit == 1){
                        holes[k][0] = i;
                        holes[k][1] = j;
                        k++;
                    }
                }
            }
            holesRep = String.format("%d,%d,%d,%d",holes[0][0],holes[0][1],holes[1][0],holes[1][1]);
            counters.putIfAbsent(holesRep, 0);
            counters.put(holesRep, counters.get(holesRep) + 1);
        }

        File file = new File("fastData.txt");
        FileWriter fr = new FileWriter(file, true);;
        String outstr = "";
        int[] is, js;
        for (int i = 0; i < 42; i++){
            for (int j = i + 1; j < 43; j++){
                is = possibleBlockers[i];
                js = possibleBlockers[j];
                holesRep = String.format("%d,%d,%d,%d",is[0],is[1],js[0],js[1]);
                counters.putIfAbsent(holesRep, 0);
                outstr = String.format(holesRep + ",%d\n", counters.get(holesRep));
                fr.write(outstr);
            }
        }
        fr.close();
    }
}
