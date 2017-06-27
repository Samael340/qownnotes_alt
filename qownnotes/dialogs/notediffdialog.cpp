#include "notediffdialog.h"
#include "ui_notediffdialog.h"
#include <QPushButton>
#include <QDialogButtonBox>
#include <QAbstractButton>
#include <QDebug>
#include <QSettings>
#include <QTimer>

NoteDiffDialog::NoteDiffDialog(QWidget *parent, QString html) :
        MasterDialog(parent),
        ui(new Ui::NoteDiffDialog) {
    ui->setupUi(this);

    _notificationButtonGroup = new QButtonGroup(this);
    _notificationButtonGroup->addButton(ui->ignoreAllExternalChangesCheckBox);
    _notificationButtonGroup->addButton(ui->acceptAllExternalChangesCheckBox);

    // create a hidden checkbox so we can un-check above checkboxes
    _notificationNoneCheckBox = new QCheckBox(this);
    _notificationNoneCheckBox->setHidden(true);
    _notificationButtonGroup->addButton(_notificationNoneCheckBox);
    connect(_notificationButtonGroup,
            SIGNAL(buttonPressed(QAbstractButton *)),
            this, SLOT(notificationButtonGroupPressed(QAbstractButton *)));

    this->ui->textEdit->setHtml(html);

    QPushButton *button;
    ui->buttonBox->clear();

    button = new QPushButton(tr("Yes"));
    button->setProperty("ActionRole", Reload);
    button->setDefault(false);
    ui->buttonBox->addButton(button, QDialogButtonBox::ActionRole);

    button = new QPushButton(tr("No"));
    button->setProperty("ActionRole", Overwrite);
    button->setDefault(false);
    ui->buttonBox->addButton(button, QDialogButtonBox::ActionRole);

//    button = new QPushButton(tr("&Ignore changes"));
//    button->setProperty("ActionRole", Ignore);
//    button->setDefault(true);
//    ui->buttonBox->addButton(button, QDialogButtonBox::ActionRole);
//
//    button = new QPushButton(tr("&Cancel"));
//    button->setProperty("ActionRole", Cancel);
//    button->setDefault(false);
//    ui->buttonBox->addButton(button, QDialogButtonBox::ActionRole);

    connect(this->ui->buttonBox, SIGNAL(clicked(QAbstractButton *)),
            SLOT(dialogButtonClicked(QAbstractButton *)));
}

NoteDiffDialog::~NoteDiffDialog() {
    delete ui;
}

/**
 * Check the _notificationNoneCheckBox when the checkboxes should all be
 * unchecked
 *
 * @param button
 */
void NoteDiffDialog::notificationButtonGroupPressed(
        QAbstractButton *button) {
    if (button->isChecked()) {
        QTimer::singleShot(100, this,
                           SLOT(notificationNoneCheckBoxCheck()));
    }
}

/**
 * Check the _notificationNoneCheckBox
 */
void NoteDiffDialog::notificationNoneCheckBoxCheck() {
    _notificationNoneCheckBox->setChecked(true);
}

void NoteDiffDialog::dialogButtonClicked(QAbstractButton *button) {
    this->actionRole = button->property("ActionRole").toInt();

    // set the setting to ignore all external changes
    if (ui->ignoreAllExternalChangesCheckBox->isChecked()) {
        QSettings settings;
        settings.setValue("ignoreAllExternalModifications", true);
    }

    // set the setting to accept all external changes
    if (ui->acceptAllExternalChangesCheckBox->isChecked()) {
        QSettings settings;
        settings.setValue("acceptAllExternalModifications", true);
    }

    this->close();
}

int NoteDiffDialog::resultActionRole() {
    return this->actionRole;
}