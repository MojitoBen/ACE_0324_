using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using static System.Runtime.CompilerServices.RuntimeHelpers;
using static System.Windows.Forms.VisualStyles.VisualStyleElement.StartPanel;
using static ace_access_system.Static_Class;

namespace ace_access_system
{
    public partial class Form_Login : Form
    {
        public static string LoggedInAccount { get; private set; }
        public Form_Login()
        {
            InitializeComponent();
            textBox_password.KeyPress += TextBoxHelper.Passwd_Keypress;
            textBox_account.ImeMode = ImeMode.Off;
        }

        private void Form_Login_Load(object sender, EventArgs e)
        {
#pragma warning disable CS8622
            textBox_account.KeyDown += TextBoxEnter_KeyDown;
            textBox_password.KeyDown += TextBoxEnter_KeyDown;
        }

        private void button_leave_Click(object sender, EventArgs e)
        {
            DialogResult result = MessageBox.Show("確認離開程式", "結束", MessageBoxButtons.YesNo, MessageBoxIcon.Warning);

            if (result == DialogResult.Yes)
            {
                Application.Exit();
            }
        }

        private void button_login_Click(object sender, EventArgs e)
        {
            AccountValidator validator = new();
            string account = textBox_account.Text.Trim();
            string password = textBox_password.Text.Trim();

            if (string.IsNullOrEmpty(account))
            {
                MessageBox.Show("請輸入帳號", "錯誤", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }


            if (string.IsNullOrEmpty(password))
            {
                MessageBox.Show("請輸入密碼", "錯誤", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            if (validator.Validate(account, password))
            {
                LoggedInAccount = account;
                Debug.WriteLine("LoggedInAccount:" + LoggedInAccount);
                MainForm mainForm = new MainForm();
                mainForm.Show();
                this.Hide();
            }

            else
            {
                LogRecord.WriteLog(textBox_account.Text + "\n" + textBox_password.Text, "form_login");
                MessageBox.Show("請確認帳號密碼", "錯誤", MessageBoxButtons.OK, MessageBoxIcon.Error);
                Debug.WriteLine(textBox_account.Text);
                Debug.WriteLine(textBox_password.Text);
                textBox_account.Clear();
                textBox_password.Clear();
            }

        }

        private void textBox_password_TextChanged(object sender, EventArgs e)
        {

        }
        private void TextBoxEnter_KeyDown(object sender, KeyEventArgs e)
        {
            if (e.KeyCode == Keys.Enter)
            {
                button_login.PerformClick();

            }
        }

        private void textBox_account_TextChanged(object sender, EventArgs e)
        {
            textBox_password.UseSystemPasswordChar = true; // 隱藏密碼輸入
            textBox_password.PasswordChar = '●'; // 密碼顯示為 '●'
        }

        private void checkBox_showpsd_CheckedChanged(object sender, EventArgs e)
        {
            if (checkBox_showpsd.Checked)
            {
                textBox_password.UseSystemPasswordChar = false;
                textBox_password.PasswordChar = '\0';
            }
            else
            {
                textBox_password.UseSystemPasswordChar = true;
                textBox_password.PasswordChar = '●'; // 密碼顯示為 '●'
            }
        }

    }
}
