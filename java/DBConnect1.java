import java.sql.*;

public class DBConnect1 {
     public static void main(String[] args) throws Exception {

          /* 1) PostgreSQL�ւ̐ڑ���� */
          Connection con; 
          Statement st;
          ResultSet rs;

          String url = "jdbc:postgresql://localhost:5432/postgres";
          String user = "postgres";
          String password = "test"; 

          /* 2) JDBC�h���C�o�̒�` */
          Class.forName("org.postgresql.Driver");

          /* 3) PostgreSQL�ւ̐ڑ� */
          con = DriverManager.getConnection(url, user, password);
          st = con.createStatement();

          /* 4) SELECT���̎��s */
          rs = st.executeQuery("SELECT 1 AS col_1");

          /* 5) ���ʂ̉�ʕ\�� */
          rs.next(); 
          System.out.print(rs.getInt("col_1"));

          /* 6) PostgreSQL�Ƃ̐ڑ���ؒf */
          rs.close(); 
          st.close();
          con.close();
     }
}