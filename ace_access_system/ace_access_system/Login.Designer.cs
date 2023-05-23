namespace ace_access_system
{
    partial class Form_Login
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            panel_login = new Panel();
            button_login = new Button();
            button_leave = new Button();
            label_pwd = new Label();
            label_account = new Label();
            textBox_password = new TextBox();
            textBox_account = new TextBox();
            checkBox_showpsd = new CheckBox();
            panel_login.SuspendLayout();
            SuspendLayout();
            // 
            // panel_login
            // 
            panel_login.BackColor = Color.LightBlue;
            panel_login.Controls.Add(checkBox_showpsd);
            panel_login.Controls.Add(button_login);
            panel_login.Controls.Add(button_leave);
            panel_login.Controls.Add(label_pwd);
            panel_login.Controls.Add(label_account);
            panel_login.Controls.Add(textBox_password);
            panel_login.Controls.Add(textBox_account);
            panel_login.Dock = DockStyle.Fill;
            panel_login.Location = new Point(0, 0);
            panel_login.Name = "panel_login";
            panel_login.Size = new Size(555, 361);
            panel_login.TabIndex = 0;
            // 
            // button_login
            // 
            button_login.Font = new Font("微軟正黑體", 20.25F, FontStyle.Bold, GraphicsUnit.Point);
            button_login.Location = new Point(110, 259);
            button_login.Name = "button_login";
            button_login.Size = new Size(129, 50);
            button_login.TabIndex = 6;
            button_login.Text = "登入";
            button_login.UseVisualStyleBackColor = true;
            button_login.Click += button_login_Click;
            // 
            // button_leave
            // 
            button_leave.Font = new Font("微軟正黑體", 20.25F, FontStyle.Bold, GraphicsUnit.Point);
            button_leave.Location = new Point(304, 259);
            button_leave.Name = "button_leave";
            button_leave.Size = new Size(129, 50);
            button_leave.TabIndex = 5;
            button_leave.Text = "退出";
            button_leave.UseVisualStyleBackColor = true;
            button_leave.Click += button_leave_Click;
            // 
            // label_pwd
            // 
            label_pwd.AutoSize = true;
            label_pwd.Font = new Font("微軟正黑體", 20.25F, FontStyle.Bold, GraphicsUnit.Point);
            label_pwd.Location = new Point(110, 161);
            label_pwd.Name = "label_pwd";
            label_pwd.Size = new Size(69, 35);
            label_pwd.TabIndex = 3;
            label_pwd.Text = "密碼";
            // 
            // label_account
            // 
            label_account.AutoSize = true;
            label_account.Font = new Font("微軟正黑體", 20.25F, FontStyle.Bold, GraphicsUnit.Point);
            label_account.Location = new Point(110, 82);
            label_account.Name = "label_account";
            label_account.Size = new Size(69, 35);
            label_account.TabIndex = 2;
            label_account.Text = "帳號";
            // 
            // textBox_password
            // 
            textBox_password.Font = new Font("Calibri", 20.25F, FontStyle.Regular, GraphicsUnit.Point);
            textBox_password.Location = new Point(222, 159);
            textBox_password.Name = "textBox_password";
            textBox_password.Size = new Size(211, 40);
            textBox_password.TabIndex = 1;
            textBox_password.TextChanged += textBox_password_TextChanged;
            // 
            // textBox_account
            // 
            textBox_account.Font = new Font("Calibri", 20.25F, FontStyle.Regular, GraphicsUnit.Point);
            textBox_account.Location = new Point(222, 80);
            textBox_account.Name = "textBox_account";
            textBox_account.Size = new Size(211, 40);
            textBox_account.TabIndex = 0;
            textBox_account.TextChanged += textBox_account_TextChanged;
            // 
            // checkBox_showpsd
            // 
            checkBox_showpsd.AutoSize = true;
            checkBox_showpsd.Font = new Font("微軟正黑體", 12F, FontStyle.Bold, GraphicsUnit.Point);
            checkBox_showpsd.Location = new Point(450, 171);
            checkBox_showpsd.Name = "checkBox_showpsd";
            checkBox_showpsd.Size = new Size(93, 25);
            checkBox_showpsd.TabIndex = 7;
            checkBox_showpsd.Text = "顯示密碼";
            checkBox_showpsd.UseVisualStyleBackColor = true;
            checkBox_showpsd.CheckedChanged += checkBox_showpsd_CheckedChanged;
            // 
            // Form_Login
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(555, 361);
            Controls.Add(panel_login);
            Name = "Form_Login";
            StartPosition = FormStartPosition.CenterScreen;
            Text = "登入";
            Load += Form_Login_Load;
            panel_login.ResumeLayout(false);
            panel_login.PerformLayout();
            ResumeLayout(false);
        }

        #endregion

        private Panel panel_login;
        private TextBox textBox_password;
        private TextBox textBox_account;
        private Label label_pwd;
        private Label label_account;
        private Button button_leave;
        private Button button_login;
        private CheckBox checkBox_showpsd;
    }
}