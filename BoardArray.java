import java.util.LinkedList;

public class BoardArray {
    LinkedList<BoardPieces> boards;
    char[] reps;
    int piecesUsed;

    public BoardArray(BoardPieces board){
        boards = new LinkedList<BoardPieces>();
        boards.add(board);
        piecesUsed = 0;
        reps = new char[8];
    }

    public BoardArray(Board board){
        boards = new LinkedList<BoardPieces>();
        boards.add(new BoardPieces(board));
        piecesUsed = 0;
        reps = new char[8];
    }

    // copy constructor
    public BoardArray(LinkedList<BoardPieces> boards, char[] reps, int piecesUsed){
        this.boards = boards;
        this.piecesUsed = piecesUsed;
        this.reps = new char[8];
        for (int i = 0; i < reps.length; i++) {
            this.reps[i] = reps[i];
        }
    }

    public void add(BoardArray newArray){
        boards.addAll(newArray.boards);
    }

    public void printAll(){
        for (BoardPieces board : boards) {
            board.print(this.reps, this.piecesUsed);
            System.out.println();
        }
    }

    public BoardArray tryPiece(Piece piece) {
        LinkedList<BoardPieces> newBoards = new LinkedList<BoardPieces>();
        for (BoardPieces board : boards) {
            newBoards.addAll(board.tryPiece(piece, this.piecesUsed));
        } 
        reps[this.piecesUsed] = piece.rep;
        return new BoardArray(newBoards, this.reps, this.piecesUsed + 1);
    }

    public int length(){
        return this.boards.size();
    }
}
