namespace ace_access_system
{
    partial class Form_Register
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
            label_account = new Label();
            label1 = new Label();
            label2 = new Label();
            textBox_account = new TextBox();
            textBox_pwd = new TextBox();
            textBox_ensure = new TextBox();
            button_enter = new Button();
            button_cancel = new Button();
            SuspendLayout();
            // 
            // label_account
            // 
            label_account.AutoSize = true;
            label_account.Font = new Font("微軟正黑體", 20.25F, FontStyle.Bold, GraphicsUnit.Point);
            label_account.Location = new Point(122, 81);
            label_account.Name = "label_account";
            label_account.Size = new Size(69, 35);
            label_account.TabIndex = 3;
            label_account.Text = "帳號";
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Font = new Font("微軟正黑體", 20.25F, FontStyle.Bold, GraphicsUnit.Point);
            label1.Location = new Point(95, 167);
            label1.Name = "label1";
            label1.Size = new Size(96, 35);
            label1.TabIndex = 4;
            label1.Text = "新密碼";
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Font = new Font("微軟正黑體", 20.25F, FontStyle.Bold, GraphicsUnit.Point);
            label2.Location = new Point(41, 259);
            label2.Name = "label2";
            label2.Size = new Size(150, 35);
            label2.TabIndex = 5;
            label2.Text = "確認新密碼";
            // 
            // textBox_account
            // 
            textBox_account.Font = new Font("Calibri", 20.25F, FontStyle.Regular, GraphicsUnit.Point);
            textBox_account.Location = new Point(222, 81);
            textBox_account.Name = "textBox_account";
            textBox_account.Size = new Size(211, 40);
            textBox_account.TabIndex = 6;
            // 
            // textBox_pwd
            // 
            textBox_pwd.Font = new Font("Calibri", 20.25F, FontStyle.Regular, GraphicsUnit.Point);
            textBox_pwd.Location = new Point(222, 167);
            textBox_pwd.Name = "textBox_pwd";
            textBox_pwd.Size = new Size(211, 40);
            textBox_pwd.TabIndex = 7;
            textBox_pwd.TextChanged += textBox_pwd_TextChanged;
            // 
            // textBox_ensure
            // 
            textBox_ensure.Font = new Font("Calibri", 20.25F, FontStyle.Regular, GraphicsUnit.Point);
            textBox_ensure.Location = new Point(222, 254);
            textBox_ensure.Name = "textBox_ensure";
            textBox_ensure.Size = new Size(211, 40);
            textBox_ensure.TabIndex = 8;
            textBox_ensure.TextChanged += textBox_ensure_TextChanged;
            // 
            // button_enter
            // 
            button_enter.Font = new Font("微軟正黑體", 20.25F, FontStyle.Bold, GraphicsUnit.Point);
            button_enter.Location = new Point(95, 367);
            button_enter.Name = "button_enter";
            button_enter.Size = new Size(129, 50);
            button_enter.TabIndex = 9;
            button_enter.Text = "確認";
            button_enter.UseVisualStyleBackColor = true;
            button_enter.Click += button_enter_Click;
            // 
            // button_cancel
            // 
            button_cancel.Font = new Font("微軟正黑體", 20.25F, FontStyle.Bold, GraphicsUnit.Point);
            button_cancel.Location = new Point(304, 367);
            button_cancel.Name = "button_cancel";
            button_cancel.Size = new Size(129, 50);
            button_cancel.TabIndex = 10;
            button_cancel.Text = "取消";
            button_cancel.UseVisualStyleBackColor = true;
            button_cancel.Click += button_cancel_Click;
            // 
            // Form_Register
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            BackColor = Color.LightBlue;
            ClientSize = new Size(555, 461);
            Controls.Add(button_cancel);
            Controls.Add(button_enter);
            Controls.Add(textBox_ensure);
            Controls.Add(textBox_pwd);
            Controls.Add(textBox_account);
            Controls.Add(label2);
            Controls.Add(label1);
            Controls.Add(label_account);
            Name = "Form_Register";
            StartPosition = FormStartPosition.CenterScreen;
            Text = "註冊使用者";
            Load += Form_Register_Load;
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Label label_account;
        private Label label1;
        private Label label2;
        private TextBox textBox_account;
        private TextBox textBox_pwd;
        private TextBox textBox_ensure;
        private Button button_enter;
        private Button button_cancel;
    }
}