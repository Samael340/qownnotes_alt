#pragma once

#include "masterdialog.h"
#include <QDialog>

namespace Ui {
class WelcomeDialog;
}

class WelcomeDialog : public MasterDialog
{
    Q_OBJECT

public:
    enum WelcomePages {
        NoteFolderPage,
        OwnCloudPage,
        MetricsPage
    };

    explicit WelcomeDialog(QWidget *parent = 0);
    ~WelcomeDialog();

private slots:
    void on_cancelButton_clicked();

    void on_nextButton_clicked();

    void on_backButton_clicked();

    void on_finishButton_clicked();

    void on_noteFolderButton_clicked();

    void on_ownCloudSettingsButton_clicked();

    void on_networkSettingsButton_clicked();

private:
    Ui::WelcomeDialog *ui;
    bool _allowFinishButton;
    QString _notesPath;

    bool handleNoteFolderSetup();

    void showNoteFolderErrorMessage(QString message);

    void storeNoteFolderSettings();

    void closeEvent(QCloseEvent *event);
};
