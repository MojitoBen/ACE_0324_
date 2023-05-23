namespace ace_access_system
{
    partial class Form_Permission
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form_Permission));
            DataGridViewCellStyle dataGridViewCellStyle1 = new DataGridViewCellStyle();
            DataGridViewCellStyle dataGridViewCellStyle2 = new DataGridViewCellStyle();
            DataGridViewCellStyle dataGridViewCellStyle3 = new DataGridViewCellStyle();
            DataGridViewCellStyle dataGridViewCellStyle4 = new DataGridViewCellStyle();
            DataGridViewCellStyle dataGridViewCellStyle5 = new DataGridViewCellStyle();
            DataGridViewCellStyle dataGridViewCellStyle6 = new DataGridViewCellStyle();
            DataGridViewCellStyle dataGridViewCellStyle7 = new DataGridViewCellStyle();
            DataGridViewCellStyle dataGridViewCellStyle8 = new DataGridViewCellStyle();
            DataGridViewCellStyle dataGridViewCellStyle9 = new DataGridViewCellStyle();
            DataGridViewCellStyle dataGridViewCellStyle10 = new DataGridViewCellStyle();
            DataGridViewCellStyle dataGridViewCellStyle11 = new DataGridViewCellStyle();
            button_cancel = new Button();
            comboBox_AreaC = new ComboBox();
            panel_check = new Panel();
            panel1 = new Panel();
            radioButton_OffC = new RadioButton();
            radioButton_OnC = new RadioButton();
            label7 = new Label();
            numericUpDown_DoorNumC = new NumericUpDown();
            comboBox_WayC = new ComboBox();
            button_check = new Button();
            button_ClearC = new Button();
            textBox_IDC = new TextBox();
            button_Area_Manage = new Button();
            label4 = new Label();
            label3 = new Label();
            label2 = new Label();
            label1 = new Label();
            button_enter = new Button();
            button_clear = new Button();
            button_export = new Button();
            button_del = new Button();
            button_revise = new Button();
            button_add = new Button();
            button_close = new Button();
            panel_Device = new Panel();
            textBox_Info = new TextBox();
            label6 = new Label();
            panel_authC = new Panel();
            radioButton_Off = new RadioButton();
            radioButton_On = new RadioButton();
            label5 = new Label();
            numericUpDown_DoorNum = new NumericUpDown();
            listbox_Doors = new ListBox();
            label12 = new Label();
            comboBox_Area = new ComboBox();
            label11 = new Label();
            comboBox_Way = new ComboBox();
            textBox_ID = new TextBox();
            label10 = new Label();
            label9 = new Label();
            label8 = new Label();
            dataGridView_SQL = new DataGridView();
            Column1 = new DataGridViewTextBoxColumn();
            Column2 = new DataGridViewTextBoxColumn();
            Column3 = new DataGridViewTextBoxColumn();
            Column4 = new DataGridViewTextBoxColumn();
            Column5 = new DataGridViewTextBoxColumn();
            Column9 = new DataGridViewTextBoxColumn();
            Column6 = new DataGridViewTextBoxColumn();
            Column7 = new DataGridViewTextBoxColumn();
            Column8 = new DataGridViewTextBoxColumn();
            panel_IP = new Panel();
            numericUpDown_Port = new NumericUpDown();
            label14 = new Label();
            textBox_IP = new TextBox();
            label13 = new Label();
            button1 = new Button();
            panel_check.SuspendLayout();
            panel1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)numericUpDown_DoorNumC).BeginInit();
            panel_Device.SuspendLayout();
            panel_authC.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)numericUpDown_DoorNum).BeginInit();
            ((System.ComponentModel.ISupportInitialize)dataGridView_SQL).BeginInit();
            panel_IP.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)numericUpDown_Port).BeginInit();
            SuspendLayout();
            // 
            // button_cancel
            // 
            button_cancel.Font = new Font("微軟正黑體", 12F, FontStyle.Bold, GraphicsUnit.Point);
            button_cancel.Location = new Point(271, 511);
            button_cancel.Name = "button_cancel";
            button_cancel.Size = new Size(134, 43);
            button_cancel.TabIndex = 60;
            button_cancel.Text = "取消";
            button_cancel.UseVisualStyleBackColor = true;
            button_cancel.Click += button_cancel_Click;
            // 
            // comboBox_AreaC
            // 
            comboBox_AreaC.Font = new Font("微軟正黑體", 12F, FontStyle.Regular, GraphicsUnit.Point);
            comboBox_AreaC.FormattingEnabled = true;
            comboBox_AreaC.Location = new Point(99, 176);
            comboBox_AreaC.Name = "comboBox_AreaC";
            comboBox_AreaC.Size = new Size(156, 28);
            comboBox_AreaC.TabIndex = 19;
            // 
            // panel_check
            // 
            panel_check.Controls.Add(panel1);
            panel_check.Controls.Add(label7);
            panel_check.Controls.Add(numericUpDown_DoorNumC);
            panel_check.Controls.Add(comboBox_WayC);
            panel_check.Controls.Add(button_check);
            panel_check.Controls.Add(button_ClearC);
            panel_check.Controls.Add(comboBox_AreaC);
            panel_check.Controls.Add(textBox_IDC);
            panel_check.Controls.Add(button_Area_Manage);
            panel_check.Controls.Add(label4);
            panel_check.Controls.Add(label3);
            panel_check.Controls.Add(label2);
            panel_check.Controls.Add(label1);
            panel_check.Location = new Point(-4, -3);
            panel_check.Name = "panel_check";
            panel_check.Size = new Size(430, 339);
            panel_check.TabIndex = 18;
            // 
            // panel1
            // 
            panel1.Controls.Add(radioButton_OffC);
            panel1.Controls.Add(radioButton_OnC);
            panel1.Location = new Point(99, 219);
            panel1.Name = "panel1";
            panel1.Size = new Size(156, 35);
            panel1.TabIndex = 76;
            // 
            // radioButton_OffC
            // 
            radioButton_OffC.AutoSize = true;
            radioButton_OffC.Font = new Font("微軟正黑體", 12F, FontStyle.Bold, GraphicsUnit.Point);
            radioButton_OffC.Location = new Point(77, 3);
            radioButton_OffC.Name = "radioButton_OffC";
            radioButton_OffC.Size = new Size(76, 25);
            radioButton_OffC.TabIndex = 1;
            radioButton_OffC.Text = "關閉中";
            radioButton_OffC.UseVisualStyleBackColor = true;
            // 
            // radioButton_OnC
            // 
            radioButton_OnC.AutoSize = true;
            radioButton_OnC.Checked = true;
            radioButton_OnC.Font = new Font("微軟正黑體", 12F, FontStyle.Bold, GraphicsUnit.Point);
            radioButton_OnC.Location = new Point(8, 3);
            radioButton_OnC.Name = "radioButton_OnC";
            radioButton_OnC.Size = new Size(76, 25);
            radioButton_OnC.TabIndex = 0;
            radioButton_OnC.TabStop = true;
            radioButton_OnC.Text = "使用中";
            radioButton_OnC.UseVisualStyleBackColor = true;
            // 
            // label7
            // 
            label7.AutoSize = true;
            label7.Font = new Font("微軟正黑體", 12F, FontStyle.Bold, GraphicsUnit.Point);
            label7.Location = new Point(12, 227);
            label7.Name = "label7";
            label7.Size = new Size(74, 21);
            label7.TabIndex = 73;
            label7.Text = "使用狀態";
            // 
            // numericUpDown_DoorNumC
            // 
            numericUpDown_DoorNumC.Font = new Font("微軟正黑體", 12F, FontStyle.Bold, GraphicsUnit.Point);
            numericUpDown_DoorNumC.Location = new Point(99, 79);
            numericUpDown_DoorNumC.Maximum = new decimal(new int[] { 10000, 0, 0, 0 });
            numericUpDown_DoorNumC.Name = "numericUpDown_DoorNumC";
            numericUpDown_DoorNumC.Size = new Size(84, 29);
            numericUpDown_DoorNumC.TabIndex = 72;
            numericUpDown_DoorNumC.Value = new decimal(new int[] { 1, 0, 0, 0 });
            // 
            // comboBox_WayC
            // 
            comboBox_WayC.Font = new Font("微軟正黑體", 12F, FontStyle.Regular, GraphicsUnit.Point);
            comboBox_WayC.FormattingEnabled = true;
            comboBox_WayC.Items.AddRange(new object[] { "雙向", "只進", "只出", "關閉" });
            comboBox_WayC.Location = new Point(99, 125);
            comboBox_WayC.Name = "comboBox_WayC";
            comboBox_WayC.Size = new Size(156, 28);
            comboBox_WayC.TabIndex = 21;
            // 
            // button_check
            // 
            button_check.Font = new Font("微軟正黑體", 24F, FontStyle.Bold, GraphicsUnit.Point);
            button_check.Image = (Image)resources.GetObject("button_check.Image");
            button_check.Location = new Point(261, 0);
            button_check.Name = "button_check";
            button_check.Size = new Size(169, 200);
            button_check.TabIndex = 13;
            button_check.Text = "查詢";
            button_check.TextAlign = ContentAlignment.BottomCenter;
            button_check.TextImageRelation = TextImageRelation.ImageAboveText;
            button_check.UseVisualStyleBackColor = true;
            button_check.Click += button_check_Click;
            // 
            // button_ClearC
            // 
            button_ClearC.Font = new Font("微軟正黑體", 24F, FontStyle.Bold, GraphicsUnit.Point);
            button_ClearC.Image = (Image)resources.GetObject("button_ClearC.Image");
            button_ClearC.ImageAlign = ContentAlignment.TopCenter;
            button_ClearC.Location = new Point(261, 199);
            button_ClearC.Name = "button_ClearC";
            button_ClearC.Size = new Size(169, 137);
            button_ClearC.TabIndex = 20;
            button_ClearC.Text = "清除";
            button_ClearC.TextAlign = ContentAlignment.BottomCenter;
            button_ClearC.TextImageRelation = TextImageRelation.ImageAboveText;
            button_ClearC.UseVisualStyleBackColor = true;
            button_ClearC.Click += button_ClearC_Click;
            // 
            // textBox_IDC
            // 
            textBox_IDC.Font = new Font("微軟正黑體", 12F, FontStyle.Regular, GraphicsUnit.Point);
            textBox_IDC.Location = new Point(99, 29);
            textBox_IDC.Name = "textBox_IDC";
            textBox_IDC.Size = new Size(156, 29);
            textBox_IDC.TabIndex = 7;
            // 
            // button_Area_Manage
            // 
            button_Area_Manage.Font = new Font("微軟正黑體", 12F, FontStyle.Bold, GraphicsUnit.Point);
            button_Area_Manage.Location = new Point(26, 268);
            button_Area_Manage.Name = "button_Area_Manage";
            button_Area_Manage.Size = new Size(219, 42);
            button_Area_Manage.TabIndex = 67;
            button_Area_Manage.Text = "控制器區域管理";
            button_Area_Manage.UseVisualStyleBackColor = true;
            button_Area_Manage.Click += button_Area_Manage_Click;
            // 
            // label4
            // 
            label4.AutoSize = true;
            label4.Font = new Font("微軟正黑體", 12F, FontStyle.Bold, GraphicsUnit.Point);
            label4.Location = new Point(12, 179);
            label4.Name = "label4";
            label4.Size = new Size(74, 21);
            label4.TabIndex = 3;
            label4.Text = "控制區域";
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Font = new Font("微軟正黑體", 12F, FontStyle.Bold, GraphicsUnit.Point);
            label3.Location = new Point(12, 127);
            label3.Name = "label3";
            label3.Size = new Size(74, 21);
            label3.TabIndex = 2;
            label3.Text = "進出方向";
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Font = new Font("微軟正黑體", 12F, FontStyle.Bold, GraphicsUnit.Point);
            label2.Location = new Point(12, 79);
            label2.Name = "label2";
            label2.Size = new Size(74, 21);
            label2.TabIndex = 1;
            label2.Text = "控制門數";
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Font = new Font("微軟正黑體", 12F, FontStyle.Bold, GraphicsUnit.Point);
            label1.Location = new Point(11, 32);
            label1.Name = "label1";
            label1.Size = new Size(75, 21);
            label1.TabIndex = 0;
            label1.Text = "控制器ID";
            // 
            // button_enter
            // 
            button_enter.Font = new Font("微軟正黑體", 12F, FontStyle.Bold, GraphicsUnit.Point);
            button_enter.Location = new Point(70, 511);
            button_enter.Name = "button_enter";
            button_enter.Size = new Size(134, 43);
            button_enter.TabIndex = 59;
            button_enter.Text = "確定";
            button_enter.UseVisualStyleBackColor = true;
            button_enter.Click += button_enter_Click;
            // 
            // button_clear
            // 
            button_clear.Font = new Font("微軟正黑體", 24F, FontStyle.Bold, GraphicsUnit.Point);
            button_clear.Image = (Image)resources.GetObject("button_clear.Image");
            button_clear.ImageAlign = ContentAlignment.TopCenter;
            button_clear.Location = new Point(257, 161);
            button_clear.Name = "button_clear";
            button_clear.Size = new Size(169, 119);
            button_clear.TabIndex = 23;
            button_clear.Text = "清除";
            button_clear.TextAlign = ContentAlignment.BottomCenter;
            button_clear.TextImageRelation = TextImageRelation.ImageAboveText;
            button_clear.UseVisualStyleBackColor = true;
            // 
            // button_export
            // 
            button_export.Font = new Font("微軟正黑體", 24F, FontStyle.Bold, GraphicsUnit.Point);
            button_export.Image = (Image)resources.GetObject("button_export.Image");
            button_export.ImageAlign = ContentAlignment.MiddleLeft;
            button_export.Location = new Point(971, -3);
            button_export.Name = "button_export";
            button_export.Size = new Size(175, 100);
            button_export.TabIndex = 21;
            button_export.Text = "導出";
            button_export.TextAlign = ContentAlignment.MiddleRight;
            button_export.TextImageRelation = TextImageRelation.ImageBeforeText;
            button_export.UseVisualStyleBackColor = true;
            button_export.Click += button_export_Click;
            // 
            // button_del
            // 
            button_del.Font = new Font("微軟正黑體", 24F, FontStyle.Bold, GraphicsUnit.Point);
            button_del.Image = (Image)resources.GetObject("button_del.Image");
            button_del.ImageAlign = ContentAlignment.MiddleLeft;
            button_del.Location = new Point(789, -3);
            button_del.Name = "button_del";
            button_del.Size = new Size(185, 100);
            button_del.TabIndex = 20;
            button_del.Text = "刪除";
            button_del.TextAlign = ContentAlignment.MiddleRight;
            button_del.UseVisualStyleBackColor = true;
            button_del.Click += button_del_Click;
            // 
            // button_revise
            // 
            button_revise.Font = new Font("微軟正黑體", 24F, FontStyle.Bold, GraphicsUnit.Point);
            button_revise.Image = (Image)resources.GetObject("button_revise.Image");
            button_revise.ImageAlign = ContentAlignment.MiddleLeft;
            button_revise.Location = new Point(610, -3);
            button_revise.Name = "button_revise";
            button_revise.Size = new Size(186, 100);
            button_revise.TabIndex = 19;
            button_revise.Text = "修改";
            button_revise.TextAlign = ContentAlignment.MiddleRight;
            button_revise.TextImageRelation = TextImageRelation.ImageBeforeText;
            button_revise.UseVisualStyleBackColor = true;
            button_revise.Click += button_revise_Click;
            // 
            // button_add
            // 
            button_add.Font = new Font("微軟正黑體", 24F, FontStyle.Bold, GraphicsUnit.Point);
            button_add.Image = (Image)resources.GetObject("button_add.Image");
            button_add.ImageAlign = ContentAlignment.MiddleLeft;
            button_add.Location = new Point(421, -3);
            button_add.Name = "button_add";
            button_add.Size = new Size(194, 100);
            button_add.TabIndex = 16;
            button_add.Text = "新增";
            button_add.TextAlign = ContentAlignment.MiddleRight;
            button_add.TextImageRelation = TextImageRelation.ImageBeforeText;
            button_add.UseVisualStyleBackColor = true;
            button_add.Click += button_add_Click;
            // 
            // button_close
            // 
            button_close.Font = new Font("微軟正黑體", 24F, FontStyle.Bold, GraphicsUnit.Point);
            button_close.Image = (Image)resources.GetObject("button_close.Image");
            button_close.ImageAlign = ContentAlignment.MiddleLeft;
            button_close.Location = new Point(1143, -3);
            button_close.Name = "button_close";
            button_close.Size = new Size(205, 100);
            button_close.TabIndex = 22;
            button_close.Text = "離開";
            button_close.TextAlign = ContentAlignment.MiddleRight;
            button_close.TextImageRelation = TextImageRelation.ImageBeforeText;
            button_close.UseVisualStyleBackColor = true;
            button_close.Click += button_close_Click;
            // 
            // panel_Device
            // 
            panel_Device.Controls.Add(textBox_Info);
            panel_Device.Controls.Add(label6);
            panel_Device.Controls.Add(panel_authC);
            panel_Device.Controls.Add(label5);
            panel_Device.Controls.Add(numericUpDown_DoorNum);
            panel_Device.Controls.Add(listbox_Doors);
            panel_Device.Controls.Add(label12);
            panel_Device.Controls.Add(comboBox_Area);
            panel_Device.Controls.Add(label11);
            panel_Device.Controls.Add(comboBox_Way);
            panel_Device.Controls.Add(button_cancel);
            panel_Device.Controls.Add(button_enter);
            panel_Device.Controls.Add(textBox_ID);
            panel_Device.Controls.Add(label10);
            panel_Device.Controls.Add(label9);
            panel_Device.Controls.Add(label8);
            panel_Device.Location = new Point(789, 98);
            panel_Device.Name = "panel_Device";
            panel_Device.Size = new Size(559, 633);
            panel_Device.TabIndex = 17;
            // 
            // textBox_Info
            // 
            textBox_Info.Enabled = false;
            textBox_Info.Font = new Font("微軟正黑體", 12F, FontStyle.Regular, GraphicsUnit.Point);
            textBox_Info.Location = new Point(139, 392);
            textBox_Info.Name = "textBox_Info";
            textBox_Info.Size = new Size(219, 29);
            textBox_Info.TabIndex = 77;
            // 
            // label6
            // 
            label6.AutoSize = true;
            label6.Font = new Font("微軟正黑體", 12F, FontStyle.Bold, GraphicsUnit.Point);
            label6.Location = new Point(74, 395);
            label6.Name = "label6";
            label6.Size = new Size(42, 21);
            label6.TabIndex = 76;
            label6.Text = "說明";
            // 
            // panel_authC
            // 
            panel_authC.Controls.Add(radioButton_Off);
            panel_authC.Controls.Add(radioButton_On);
            panel_authC.Location = new Point(139, 446);
            panel_authC.Name = "panel_authC";
            panel_authC.Size = new Size(219, 35);
            panel_authC.TabIndex = 75;
            // 
            // radioButton_Off
            // 
            radioButton_Off.AutoSize = true;
            radioButton_Off.Font = new Font("微軟正黑體", 12F, FontStyle.Bold, GraphicsUnit.Point);
            radioButton_Off.Location = new Point(116, 5);
            radioButton_Off.Name = "radioButton_Off";
            radioButton_Off.Size = new Size(76, 25);
            radioButton_Off.TabIndex = 1;
            radioButton_Off.Text = "關閉中";
            radioButton_Off.UseVisualStyleBackColor = true;
            // 
            // radioButton_On
            // 
            radioButton_On.AutoSize = true;
            radioButton_On.Checked = true;
            radioButton_On.Font = new Font("微軟正黑體", 12F, FontStyle.Bold, GraphicsUnit.Point);
            radioButton_On.Location = new Point(9, 5);
            radioButton_On.Name = "radioButton_On";
            radioButton_On.Size = new Size(76, 25);
            radioButton_On.TabIndex = 0;
            radioButton_On.TabStop = true;
            radioButton_On.Text = "使用中";
            radioButton_On.UseVisualStyleBackColor = true;
            // 
            // label5
            // 
            label5.AutoSize = true;
            label5.Font = new Font("微軟正黑體", 12F, FontStyle.Bold, GraphicsUnit.Point);
            label5.Location = new Point(59, 453);
            label5.Name = "label5";
            label5.Size = new Size(74, 21);
            label5.TabIndex = 74;
            label5.Text = "使用狀態";
            // 
            // numericUpDown_DoorNum
            // 
            numericUpDown_DoorNum.Enabled = false;
            numericUpDown_DoorNum.Font = new Font("微軟正黑體", 12F, FontStyle.Bold, GraphicsUnit.Point);
            numericUpDown_DoorNum.Location = new Point(139, 75);
            numericUpDown_DoorNum.Maximum = new decimal(new int[] { 10000, 0, 0, 0 });
            numericUpDown_DoorNum.Name = "numericUpDown_DoorNum";
            numericUpDown_DoorNum.Size = new Size(84, 29);
            numericUpDown_DoorNum.TabIndex = 73;
            numericUpDown_DoorNum.Value = new decimal(new int[] { 1, 0, 0, 0 });
            // 
            // listbox_Doors
            // 
            listbox_Doors.Font = new Font("微軟正黑體", 12F, FontStyle.Bold, GraphicsUnit.Point);
            listbox_Doors.FormattingEnabled = true;
            listbox_Doors.ItemHeight = 21;
            listbox_Doors.Location = new Point(138, 217);
            listbox_Doors.Name = "listbox_Doors";
            listbox_Doors.SelectionMode = SelectionMode.None;
            listbox_Doors.Size = new Size(219, 130);
            listbox_Doors.TabIndex = 66;
            // 
            // label12
            // 
            label12.AutoSize = true;
            label12.Font = new Font("微軟正黑體", 12F, FontStyle.Bold, GraphicsUnit.Point);
            label12.Location = new Point(74, 217);
            label12.Name = "label12";
            label12.Size = new Size(58, 21);
            label12.TabIndex = 65;
            label12.Text = "控制門";
            // 
            // comboBox_Area
            // 
            comboBox_Area.Font = new Font("微軟正黑體", 12F, FontStyle.Bold, GraphicsUnit.Point);
            comboBox_Area.FormattingEnabled = true;
            comboBox_Area.Location = new Point(138, 167);
            comboBox_Area.Name = "comboBox_Area";
            comboBox_Area.Size = new Size(219, 29);
            comboBox_Area.TabIndex = 64;
            comboBox_Area.Text = "區域1";
            comboBox_Area.SelectedIndexChanged += comboBox_Area_SelectedIndexChanged;
            // 
            // label11
            // 
            label11.AutoSize = true;
            label11.Font = new Font("微軟正黑體", 12F, FontStyle.Bold, GraphicsUnit.Point);
            label11.Location = new Point(58, 170);
            label11.Name = "label11";
            label11.Size = new Size(74, 21);
            label11.TabIndex = 63;
            label11.Text = "控制區域";
            // 
            // comboBox_Way
            // 
            comboBox_Way.Font = new Font("微軟正黑體", 12F, FontStyle.Bold, GraphicsUnit.Point);
            comboBox_Way.FormattingEnabled = true;
            comboBox_Way.Items.AddRange(new object[] { "雙向", "只進", "只出", "關閉" });
            comboBox_Way.Location = new Point(138, 118);
            comboBox_Way.Name = "comboBox_Way";
            comboBox_Way.Size = new Size(219, 29);
            comboBox_Way.TabIndex = 62;
            comboBox_Way.Text = "雙向";
            // 
            // textBox_ID
            // 
            textBox_ID.Enabled = false;
            textBox_ID.Font = new Font("微軟正黑體", 12F, FontStyle.Regular, GraphicsUnit.Point);
            textBox_ID.Location = new Point(138, 26);
            textBox_ID.Name = "textBox_ID";
            textBox_ID.Size = new Size(219, 29);
            textBox_ID.TabIndex = 20;
            // 
            // label10
            // 
            label10.AutoSize = true;
            label10.Font = new Font("微軟正黑體", 12F, FontStyle.Bold, GraphicsUnit.Point);
            label10.Location = new Point(58, 121);
            label10.Name = "label10";
            label10.Size = new Size(74, 21);
            label10.TabIndex = 21;
            label10.Text = "進出方向";
            // 
            // label9
            // 
            label9.AutoSize = true;
            label9.Font = new Font("微軟正黑體", 12F, FontStyle.Bold, GraphicsUnit.Point);
            label9.Location = new Point(59, 78);
            label9.Name = "label9";
            label9.Size = new Size(74, 21);
            label9.TabIndex = 20;
            label9.Text = "控制門數";
            // 
            // label8
            // 
            label8.AutoSize = true;
            label8.Font = new Font("微軟正黑體", 12F, FontStyle.Bold, GraphicsUnit.Point);
            label8.Location = new Point(57, 31);
            label8.Name = "label8";
            label8.Size = new Size(75, 21);
            label8.TabIndex = 20;
            label8.Text = "控制器ID";
            // 
            // dataGridView_SQL
            // 
            dataGridViewCellStyle1.Font = new Font("微軟正黑體", 12F, FontStyle.Bold, GraphicsUnit.Point);
            dataGridView_SQL.AlternatingRowsDefaultCellStyle = dataGridViewCellStyle1;
            dataGridView_SQL.BackgroundColor = SystemColors.Control;
            dataGridViewCellStyle2.Alignment = DataGridViewContentAlignment.MiddleLeft;
            dataGridViewCellStyle2.BackColor = SystemColors.Control;
            dataGridViewCellStyle2.Font = new Font("微軟正黑體", 12F, FontStyle.Bold, GraphicsUnit.Point);
            dataGridViewCellStyle2.ForeColor = SystemColors.WindowText;
            dataGridViewCellStyle2.SelectionBackColor = SystemColors.Highlight;
            dataGridViewCellStyle2.SelectionForeColor = SystemColors.HighlightText;
            dataGridViewCellStyle2.WrapMode = DataGridViewTriState.True;
            dataGridView_SQL.ColumnHeadersDefaultCellStyle = dataGridViewCellStyle2;
            dataGridView_SQL.ColumnHeadersHeightSizeMode = DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            dataGridView_SQL.Columns.AddRange(new DataGridViewColumn[] { Column1, Column2, Column3, Column4, Column5, Column9, Column6, Column7, Column8 });
            dataGridView_SQL.Location = new Point(-4, 327);
            dataGridView_SQL.MultiSelect = false;
            dataGridView_SQL.Name = "dataGridView_SQL";
            dataGridView_SQL.RowTemplate.Height = 25;
            dataGridView_SQL.ScrollBars = ScrollBars.Horizontal;
            dataGridView_SQL.SelectionMode = DataGridViewSelectionMode.FullRowSelect;
            dataGridView_SQL.Size = new Size(800, 401);
            dataGridView_SQL.TabIndex = 15;
            // 
            // Column1
            // 
            dataGridViewCellStyle3.Font = new Font("微軟正黑體", 12F, FontStyle.Bold, GraphicsUnit.Point);
            Column1.DefaultCellStyle = dataGridViewCellStyle3;
            Column1.Frozen = true;
            Column1.HeaderText = "控制器ID";
            Column1.Name = "Column1";
            Column1.ReadOnly = true;
            // 
            // Column2
            // 
            dataGridViewCellStyle4.Font = new Font("微軟正黑體", 12F, FontStyle.Bold, GraphicsUnit.Point);
            Column2.DefaultCellStyle = dataGridViewCellStyle4;
            Column2.HeaderText = "控制門數";
            Column2.Name = "Column2";
            Column2.ReadOnly = true;
            // 
            // Column3
            // 
            dataGridViewCellStyle5.Font = new Font("微軟正黑體", 12F, FontStyle.Bold, GraphicsUnit.Point);
            Column3.DefaultCellStyle = dataGridViewCellStyle5;
            Column3.HeaderText = "進出方向";
            Column3.Name = "Column3";
            Column3.ReadOnly = true;
            // 
            // Column4
            // 
            dataGridViewCellStyle6.Font = new Font("微軟正黑體", 12F, FontStyle.Bold, GraphicsUnit.Point);
            Column4.DefaultCellStyle = dataGridViewCellStyle6;
            Column4.HeaderText = "控制區域";
            Column4.Name = "Column4";
            Column4.ReadOnly = true;
            // 
            // Column5
            // 
            dataGridViewCellStyle7.Font = new Font("微軟正黑體", 12F, FontStyle.Bold, GraphicsUnit.Point);
            Column5.DefaultCellStyle = dataGridViewCellStyle7;
            Column5.HeaderText = "控制門";
            Column5.Name = "Column5";
            Column5.ReadOnly = true;
            Column5.Width = 200;
            // 
            // Column9
            // 
            dataGridViewCellStyle8.Font = new Font("微軟正黑體", 12F, FontStyle.Bold, GraphicsUnit.Point);
            Column9.DefaultCellStyle = dataGridViewCellStyle8;
            Column9.HeaderText = "使用狀態";
            Column9.Name = "Column9";
            Column9.ReadOnly = true;
            // 
            // Column6
            // 
            dataGridViewCellStyle9.Font = new Font("微軟正黑體", 12F, FontStyle.Bold, GraphicsUnit.Point);
            Column6.DefaultCellStyle = dataGridViewCellStyle9;
            Column6.HeaderText = "IP";
            Column6.Name = "Column6";
            Column6.ReadOnly = true;
            Column6.Width = 120;
            // 
            // Column7
            // 
            dataGridViewCellStyle10.Font = new Font("微軟正黑體", 12F, FontStyle.Bold, GraphicsUnit.Point);
            Column7.DefaultCellStyle = dataGridViewCellStyle10;
            Column7.HeaderText = "PORT";
            Column7.Name = "Column7";
            Column7.ReadOnly = true;
            // 
            // Column8
            // 
            dataGridViewCellStyle11.Font = new Font("微軟正黑體", 12F, FontStyle.Bold, GraphicsUnit.Point);
            Column8.DefaultCellStyle = dataGridViewCellStyle11;
            Column8.HeaderText = "說明";
            Column8.Name = "Column8";
            Column8.ReadOnly = true;
            // 
            // panel_IP
            // 
            panel_IP.Controls.Add(numericUpDown_Port);
            panel_IP.Controls.Add(label14);
            panel_IP.Controls.Add(textBox_IP);
            panel_IP.Controls.Add(label13);
            panel_IP.Location = new Point(421, 97);
            panel_IP.Name = "panel_IP";
            panel_IP.Size = new Size(367, 183);
            panel_IP.TabIndex = 24;
            // 
            // numericUpDown_Port
            // 
            numericUpDown_Port.Font = new Font("微軟正黑體", 12F, FontStyle.Bold, GraphicsUnit.Point);
            numericUpDown_Port.Location = new Point(106, 82);
            numericUpDown_Port.Maximum = new decimal(new int[] { int.MaxValue, 0, 0, 0 });
            numericUpDown_Port.Name = "numericUpDown_Port";
            numericUpDown_Port.Size = new Size(107, 29);
            numericUpDown_Port.TabIndex = 74;
            numericUpDown_Port.Value = new decimal(new int[] { 60000, 0, 0, 0 });
            // 
            // label14
            // 
            label14.AutoSize = true;
            label14.Font = new Font("微軟正黑體", 12F, FontStyle.Bold, GraphicsUnit.Point);
            label14.Location = new Point(32, 84);
            label14.Name = "label14";
            label14.Size = new Size(53, 21);
            label14.TabIndex = 69;
            label14.Text = "PORT";
            // 
            // textBox_IP
            // 
            textBox_IP.Font = new Font("微軟正黑體", 12F, FontStyle.Regular, GraphicsUnit.Point);
            textBox_IP.Location = new Point(106, 27);
            textBox_IP.Name = "textBox_IP";
            textBox_IP.Size = new Size(219, 29);
            textBox_IP.TabIndex = 68;
            // 
            // label13
            // 
            label13.AutoSize = true;
            label13.Font = new Font("微軟正黑體", 12F, FontStyle.Bold, GraphicsUnit.Point);
            label13.Location = new Point(47, 30);
            label13.Name = "label13";
            label13.Size = new Size(25, 21);
            label13.TabIndex = 68;
            label13.Text = "IP";
            // 
            // button1
            // 
            button1.Font = new Font("微軟正黑體", 12F, FontStyle.Bold, GraphicsUnit.Point);
            button1.Location = new Point(426, 268);
            button1.Name = "button1";
            button1.Size = new Size(365, 58);
            button1.TabIndex = 25;
            button1.Text = "更新顯示介面";
            button1.UseVisualStyleBackColor = true;
            button1.Click += button1_Click;
            // 
            // Form_Permission
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            BackColor = Color.LightBlue;
            ClientSize = new Size(1350, 729);
            Controls.Add(button1);
            Controls.Add(panel_Device);
            Controls.Add(dataGridView_SQL);
            Controls.Add(panel_check);
            Controls.Add(button_clear);
            Controls.Add(button_export);
            Controls.Add(button_del);
            Controls.Add(button_revise);
            Controls.Add(button_add);
            Controls.Add(button_close);
            Controls.Add(panel_IP);
            FormBorderStyle = FormBorderStyle.FixedSingle;
            Name = "Form_Permission";
            StartPosition = FormStartPosition.CenterScreen;
            Text = "門禁資訊";
            Load += Form_Permission_Load;
            panel_check.ResumeLayout(false);
            panel_check.PerformLayout();
            panel1.ResumeLayout(false);
            panel1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)numericUpDown_DoorNumC).EndInit();
            panel_Device.ResumeLayout(false);
            panel_Device.PerformLayout();
            panel_authC.ResumeLayout(false);
            panel_authC.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)numericUpDown_DoorNum).EndInit();
            ((System.ComponentModel.ISupportInitialize)dataGridView_SQL).EndInit();
            panel_IP.ResumeLayout(false);
            panel_IP.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)numericUpDown_Port).EndInit();
            ResumeLayout(false);
        }

        #endregion
        private Button button_cancel;
        private ComboBox comboBox_AreaC;
        private Panel panel_check;
        private Button button_check;
        private TextBox textBox_IDC;
        private Label label4;
        private Label label3;
        private Label label2;
        private Label label1;
        private Button button_enter;
        private Button button_clear;
        private Button button_export;
        private Button button_del;
        private Button button_revise;
        private Button button_add;
        private Button button_close;
        private Panel panel_Device;
        private TextBox textBox_ID;
        private Label label10;
        private Label label9;
        private Label label8;
        private DataGridView dataGridView_SQL;
        private ComboBox comboBox_Way;
        private ListBox listbox_Doors;
        private Label label12;
        private ComboBox comboBox_Area;
        private Label label11;
        private Button button_Area_Manage;
        private Panel panel_IP;
        private Label label14;
        private TextBox textBox_IP;
        private Label label13;
        private Button button_ClearC;
        private ComboBox comboBox_WayC;
        private NumericUpDown numericUpDown_DoorNumC;
        private NumericUpDown numericUpDown_DoorNum;
        private NumericUpDown numericUpDown_Port;
        private Label label5;
        private Panel panel_authC;
        private RadioButton radioButton_Off;
        private RadioButton radioButton_On;
        private TextBox textBox_Info;
        private Label label6;
        private DataGridViewTextBoxColumn Column1;
        private DataGridViewTextBoxColumn Column2;
        private DataGridViewTextBoxColumn Column3;
        private DataGridViewTextBoxColumn Column4;
        private DataGridViewTextBoxColumn Column5;
        private DataGridViewTextBoxColumn Column9;
        private DataGridViewTextBoxColumn Column6;
        private DataGridViewTextBoxColumn Column7;
        private DataGridViewTextBoxColumn Column8;
        private Label label7;
        private Panel panel1;
        private RadioButton radioButton_OffC;
        private RadioButton radioButton_OnC;
        private Button button1;
    }
}