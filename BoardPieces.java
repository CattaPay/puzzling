
import java.util.LinkedList;

public class BoardPieces {
    // contains a board plus up to 8 maps for piece positions
    long bitmap;
    long[] piecemaps;

    public BoardPieces(Board board){
        this.bitmap = board.bitmap;
        this.piecemaps = new long[8];
    }

    // copy constructor
    public BoardPieces(long bitmap, long[] piecemaps){
        this.bitmap = bitmap;
        this.piecemaps = new long[8];
        for (int i = 0; i < piecemaps.length; i++) {
            this.piecemaps[i] = piecemaps[i];
        }
    }

    public void setPiecemap(int n, long newMap){
        this.piecemaps[n] = newMap;
    }

    public void printBitmap(){
        long bit;
        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {
                bit = (bitmap >> (63 - (i * 8 + j))) & 1;
                System.out.print(bit == 1 ? "X " : "O ");
            }
            System.out.println();
        }
        System.out.println();
    }

    public LinkedList<BoardPieces> tryPiece(Piece piece, int nPiece){
        LinkedList<BoardPieces> newBoards = new LinkedList<BoardPieces>();
        BoardPieces newBoard;
        long piecemap;
        for (int orient = 0; orient < piece.nOrientations; orient++){
            for (int i = 0; i < 9-piece.heights[orient]; i++){
                for (int j = 0; j < 9-piece.widths[orient]; j++){
                    piecemap = piece.bitmaps[orient] >>> (i * 8 + j);

                    // if no collision between bitmaps, do a thing
                    if ((piecemap & bitmap) == 0){
                        newBoard = new BoardPieces((piecemap | bitmap), this.piecemaps);
                        newBoard.setPiecemap(nPiece, piecemap);
                        newBoards.add(newBoard);
                    }
                }
            }   
        }
        return newBoards;
    }

    public void print(char[] reps, int piecesUsed){
        long bit;
        Boolean flag;
        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {
                flag = Boolean.FALSE;
                for (int k = 0; k < piecesUsed; k++) {
                    bit = (piecemaps[k] >> (63 - (i * 8 + j))) & 1;
                    if (bit == 1){
                        System.out.print(reps[k] + " ");
                        flag = Boolean.TRUE;
                    }
                }
                if (!flag){
                    System.out.print("O ");
                }
            }
            System.out.println();
        }
        System.out.println();
    }

    public long findHoles(int piecesUsed) {
        long bit = 0;
        for (int k = 0; k < piecesUsed; k++){
            bit |= piecemaps[k];
        }
        return bit;
    }
    
}
