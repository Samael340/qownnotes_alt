/**
 * Bookmark header
 */


#pragma once


#include <QtCore/QString>
#include <QtCore/QJsonObject>
#include <QtCore/QVariant>
#include <QtCore/QDebug>

class Bookmark {
public:
    explicit Bookmark();
    explicit Bookmark(QString url, QString name = "",
            QStringList tagList = QStringList(), QString description = "");
    friend QDebug operator<<(QDebug dbg, const Bookmark &bookmark);
    QJsonObject jsonObject();
    static QList<Bookmark> parseBookmarks(QString text, bool withBasicUrls = false);
    static QString bookmarksWebServiceJsonText(QList<Bookmark> bookmarks);
    static QString parsedBookmarksWebServiceJsonText(QString text, bool withBasicUrls = false);

protected:
    QString name;
    QString url;
    QStringList tags;
    QString description;
};
