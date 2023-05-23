using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using MySqlConnector;
using static ace_access_system.Static_Class;

namespace ace_access_system
{
    public class SQL_Conn
    {

        static string connectionString = "host=192.168.1.185;port=3306;user id=qadmin;password=3753890;database=asc_access;charset=utf8;";
        public static MySqlConnection cn;

        static SQL_Conn()
        {
            try
            {
                // 建立 MySQL 連線
                cn = new MySqlConnection(connectionString);
                cn.Open();
            }
            catch (Exception ex)
            {
                // 顯示錯誤訊息
                MessageBox.Show($"SQL Server 不存在或拒絕訪問，請檢查資料庫是否已建立。：{ex.Message}", "錯誤", MessageBoxButtons.OK, MessageBoxIcon.Error);
                //cn = null;
            }
        }
    }


    public class AccountValidator
    {
        public bool Validate(string username, string password)
        {
            bool result = false;

            try
            {

                // 使用參數化查詢
                string query = "SELECT COUNT(*) FROM user_pwd WHERE up_uid = @username AND up_pwd = @password";
                MySqlCommand cmd = new MySqlCommand(query, SQL_Conn.cn);
                cmd.Parameters.AddWithValue("@username", username);
                cmd.Parameters.AddWithValue("@password", password);
                int count = Convert.ToInt32(cmd.ExecuteScalar());
                Debug.WriteLine("count : " + count);
                if (count > 0)
                {
                    result = true;
                }
            }
            catch (Exception ex)
            {
                LogRecord.WriteLog(ex.Message, "Validate");
            }

            Debug.WriteLine(result);
            return result;
        }
        /*
        用法
        AccountValidator validator = new AccountValidator();
        if (validator.Validate(usernameTextBox.Text, passwordTextBox.Text))
        {
            // 帳號密碼正確，程式動作
        }
        else
        {
            MessageBox.Show("輸入資料有誤");
        }

        */
    } //確認帳號密碼

    public class Permission 
    {
        public bool Time_Check(string cardNum)
        {
            MySqlCommand cmd = new MySqlCommand("SELECT `Enable`, `Start_Date`, `End_Date`, `End_Time` FROM `door_permission` WHERE `CardNum` = @CardNum", SQL_Conn.cn);
            cmd.Parameters.AddWithValue("@CardNum", cardNum);

            try
            {
                SQL_Conn.cn.Open();
                using (MySqlDataReader reader = cmd.ExecuteReader())
                {
                    if (reader.Read())
                    {
                        int enable = reader.GetInt32("Enable");

                        if (enable == 0)
                        {
                            return false;
                        }

                        DateTime startDate = reader.GetDateTime("Start_Date");
                        DateTime endDate = reader.GetDateTime("End_Date");
                        TimeSpan endTime = reader.GetTimeSpan("End_Time");

                        DateTime currentDate = DateTime.Now;

                        if (currentDate >= startDate && currentDate <= endDate)
                        {
                            DateTime currentTime = currentDate.Date.Add(endTime);

                            if (currentDate <= currentTime)
                            {
                                return true;
                            }
                        }
                    }
                }
            }
            catch (Exception ex)
            {
                LogRecord.WriteLog(ex.Message, "SQL_Conn_CanPassDoor");
            }
            finally
            {
                SQL_Conn.cn.Close();
            }

            return false;
        } //step.1 確定此卡在時限內

    }

}
