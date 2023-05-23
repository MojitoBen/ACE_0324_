namespace ace_access_system
{
    partial class MainForm
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
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
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            components = new System.ComponentModel.Container();
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(MainForm));
            button_contact = new Button();
            menuStrip1 = new MenuStrip();
            功能ToolStripMenuItem = new ToolStripMenuItem();
            用戶資訊ToolStripMenuItem = new ToolStripMenuItem();
            門禁資訊ToolStripMenuItem = new ToolStripMenuItem();
            工具ToolStripMenuItem = new ToolStripMenuItem();
            button_door_permission = new Button();
            Timer_Now = new System.Windows.Forms.Timer(components);
            label_DateTime = new Label();
            註冊修改帳號ToolStripMenuItem = new ToolStripMenuItem();
            menuStrip1.SuspendLayout();
            SuspendLayout();
            // 
            // button_contact
            // 
            button_contact.BackgroundImage = (Image)resources.GetObject("button_contact.BackgroundImage");
            button_contact.BackgroundImageLayout = ImageLayout.None;
            button_contact.Cursor = Cursors.Hand;
            button_contact.FlatStyle = FlatStyle.System;
            button_contact.Font = new Font("微軟正黑體", 24F, FontStyle.Bold, GraphicsUnit.Point);
            button_contact.Location = new Point(-2, 107);
            button_contact.Name = "button_contact";
            button_contact.Size = new Size(204, 126);
            button_contact.TabIndex = 0;
            button_contact.Text = "用戶資訊";
            button_contact.UseVisualStyleBackColor = true;
            button_contact.Click += button_contact_Click;
            // 
            // menuStrip1
            // 
            menuStrip1.Items.AddRange(new ToolStripItem[] { 功能ToolStripMenuItem, 工具ToolStripMenuItem });
            menuStrip1.Location = new Point(0, 0);
            menuStrip1.Name = "menuStrip1";
            menuStrip1.Size = new Size(1350, 24);
            menuStrip1.TabIndex = 1;
            menuStrip1.Text = "menuStrip1";
            // 
            // 功能ToolStripMenuItem
            // 
            功能ToolStripMenuItem.DropDownItems.AddRange(new ToolStripItem[] { 用戶資訊ToolStripMenuItem, 門禁資訊ToolStripMenuItem });
            功能ToolStripMenuItem.Name = "功能ToolStripMenuItem";
            功能ToolStripMenuItem.Size = new Size(43, 20);
            功能ToolStripMenuItem.Text = "功能";
            // 
            // 用戶資訊ToolStripMenuItem
            // 
            用戶資訊ToolStripMenuItem.Name = "用戶資訊ToolStripMenuItem";
            用戶資訊ToolStripMenuItem.Size = new Size(122, 22);
            用戶資訊ToolStripMenuItem.Text = "用戶資訊";
            用戶資訊ToolStripMenuItem.Click += 用戶資訊ToolStripMenuItem_Click;
            // 
            // 門禁資訊ToolStripMenuItem
            // 
            門禁資訊ToolStripMenuItem.Name = "門禁資訊ToolStripMenuItem";
            門禁資訊ToolStripMenuItem.Size = new Size(122, 22);
            門禁資訊ToolStripMenuItem.Text = "門禁資訊";
            // 
            // 工具ToolStripMenuItem
            // 
            工具ToolStripMenuItem.DropDownItems.AddRange(new ToolStripItem[] { 註冊修改帳號ToolStripMenuItem });
            工具ToolStripMenuItem.Name = "工具ToolStripMenuItem";
            工具ToolStripMenuItem.Size = new Size(43, 20);
            工具ToolStripMenuItem.Text = "工具";
            // 
            // button_door_permission
            // 
            button_door_permission.BackgroundImage = (Image)resources.GetObject("button_door_permission.BackgroundImage");
            button_door_permission.BackgroundImageLayout = ImageLayout.None;
            button_door_permission.Cursor = Cursors.Hand;
            button_door_permission.FlatStyle = FlatStyle.System;
            button_door_permission.Font = new Font("微軟正黑體", 24F, FontStyle.Bold, GraphicsUnit.Point);
            button_door_permission.Location = new Point(199, 107);
            button_door_permission.Name = "button_door_permission";
            button_door_permission.Size = new Size(204, 126);
            button_door_permission.TabIndex = 2;
            button_door_permission.Text = "門禁資訊";
            button_door_permission.UseVisualStyleBackColor = true;
            button_door_permission.Click += button_door_permission_Click;
            // 
            // label_DateTime
            // 
            label_DateTime.AutoSize = true;
            label_DateTime.Font = new Font("微軟正黑體", 20.25F, FontStyle.Bold, GraphicsUnit.Point);
            label_DateTime.Location = new Point(12, 50);
            label_DateTime.Name = "label_DateTime";
            label_DateTime.Size = new Size(140, 35);
            label_DateTime.TabIndex = 3;
            label_DateTime.Text = "DateTime";
            label_DateTime.Click += label_DateTime_Click;
            // 
            // 註冊修改帳號ToolStripMenuItem
            // 
            註冊修改帳號ToolStripMenuItem.Name = "註冊修改帳號ToolStripMenuItem";
            註冊修改帳號ToolStripMenuItem.Size = new Size(180, 22);
            註冊修改帳號ToolStripMenuItem.Text = "註冊/修改帳號";
            註冊修改帳號ToolStripMenuItem.Click += 註冊修改帳號ToolStripMenuItem_Click;
            // 
            // MainForm
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            BackColor = Color.LightBlue;
            BackgroundImage = (Image)resources.GetObject("$this.BackgroundImage");
            BackgroundImageLayout = ImageLayout.Stretch;
            ClientSize = new Size(1350, 729);
            Controls.Add(label_DateTime);
            Controls.Add(button_door_permission);
            Controls.Add(button_contact);
            Controls.Add(menuStrip1);
            DoubleBuffered = true;
            Name = "MainForm";
            StartPosition = FormStartPosition.CenterScreen;
            Text = "主畫面";
            menuStrip1.ResumeLayout(false);
            menuStrip1.PerformLayout();
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Button button_contact;
        private MenuStrip menuStrip1;
        private ToolStripMenuItem 功能ToolStripMenuItem;
        private ToolStripMenuItem 用戶資訊ToolStripMenuItem;
        private Button button_door_permission;
        private System.Windows.Forms.Timer timer1;
        private Label label_DateTime;
        private System.Windows.Forms.Timer Timer_Now;
        private ToolStripMenuItem 門禁資訊ToolStripMenuItem;
        private ToolStripMenuItem 工具ToolStripMenuItem;
        private ToolStripMenuItem 註冊修改帳號ToolStripMenuItem;
    }
}