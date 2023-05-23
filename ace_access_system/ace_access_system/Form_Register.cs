using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using static ace_access_system.Static_Class;
using MySqlConnector;

namespace ace_access_system
{
    public partial class Form_Register : Form
    {
        public Form_Register()
        {
            InitializeComponent();
        }

        private void Form_Register_Load(object sender, EventArgs e)
        {
            textBox_account.KeyDown += Form_Register_Enter;
            textBox_pwd.KeyDown += Form_Register_Enter;
            textBox_ensure.KeyDown += Form_Register_Enter;
            Renew();
        }

        private void textBox_pwd_TextChanged(object sender, EventArgs e)
        {
            textBox_pwd.UseSystemPasswordChar = true; // 隱藏密碼輸入
            textBox_pwd.PasswordChar = '●'; // 密碼顯示為 '●'
        }

        private void textBox_ensure_TextChanged(object sender, EventArgs e)
        {
            textBox_ensure.UseSystemPasswordChar = true; // 隱藏密碼輸入
            textBox_ensure.PasswordChar = '●'; // 密碼顯示為 '●'
        }

        private void button_enter_Click(object sender, EventArgs e)
        {
            AccountValidator validator = new();
            string account = textBox_account.Text.Trim();
            string password = textBox_pwd.Text.Trim();
            string ensure_password = textBox_ensure.Text.Trim();
            if (string.IsNullOrEmpty(account))
            {
                MessageBox.Show("請輸入帳號", "錯誤", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            if (string.IsNullOrEmpty(password))
            {
                MessageBox.Show("請輸入新密碼", "錯誤", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            if (string.IsNullOrEmpty(ensure_password))
            {
                MessageBox.Show("請確認新密碼", "錯誤", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            if (password != ensure_password)
            {
                MessageBox.Show("新密碼與確認密碼不一致", "錯誤", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }
            SQL_Conn.cn.Close();
            SQL_Conn.cn.Open();
            // 檢查帳號是否存在
            MySqlCommand checkCmd = new MySqlCommand("SELECT COUNT(*) FROM `user_pwd` WHERE `up_uid`=@up_uid", SQL_Conn.cn);
            checkCmd.Parameters.AddWithValue("@up_uid", account);
            int accountCount = Convert.ToInt32(checkCmd.ExecuteScalar());
            SQL_Conn.cn.Close();

            if (accountCount > 0)
            {
                SQL_Conn.cn.Close();
                SQL_Conn.cn.Open();
                // 帳號已存在，執行更新操作
                MySqlCommand updateCmd = new MySqlCommand("UPDATE `user_pwd` SET `up_pwd`=@up_pwd WHERE `up_uid`=@up_uid", SQL_Conn.cn);
                updateCmd.Parameters.AddWithValue("@up_pwd", password);
                updateCmd.Parameters.AddWithValue("@up_uid", account);
                int rowsAffected = updateCmd.ExecuteNonQuery();

                if (rowsAffected > 0)
                {
                    MessageBox.Show("密碼更新成功");
                }
                else
                {
                    MessageBox.Show("密碼更新失敗");
                }
                Renew();
                SQL_Conn.cn.Close();
            }
            else
            {
                SQL_Conn.cn.Close();
                SQL_Conn.cn.Open();
                // 新帳號，執行插入操作
                MySqlCommand insertPwdCmd = new MySqlCommand("INSERT INTO `user_pwd` (`up_uid`, `up_pwd`) VALUES (@Account, @Password)", SQL_Conn.cn);
                insertPwdCmd.Parameters.AddWithValue("@Account", account);
                insertPwdCmd.Parameters.AddWithValue("@Password", password);
                int pwdRowsAffected = insertPwdCmd.ExecuteNonQuery();

                if (pwdRowsAffected > 0)
                {
                    MessageBox.Show("新增成功");
                }
                else
                {
                    MessageBox.Show("新增失敗");
                }
                Renew();
                SQL_Conn.cn.Close();
            }
        }

        private void button_cancel_Click(object sender, EventArgs e)
        {
            this.Close();
        }
        private void Form_Register_Enter(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Enter)
            {
                button_enter.PerformClick();
            }
        }
        private void Renew() 
        {
            textBox_account.Text = string.Empty;
            textBox_pwd.Text = string.Empty;
            textBox_ensure.Text = string.Empty;
        }
    }
}

