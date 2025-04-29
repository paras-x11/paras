<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:xlink="http://www.w3.org/1999/xlink">

  <xsl:output method="html" encoding="UTF-8" indent="yes"/>

  <xsl:template match="/breakfast_menu">
    <html>
      <head>
        <title>Breakfast Menu</title>
        <style>
          body { font-family: Arial; }
          table { border-collapse: collapse; width: 100%; }
          th, td { border: 1px solid #ddd; padding: 8px; }
          th { background-color: #f2f2f2; }
        </style>
      </head>
      <body>
        <h2>Breakfast Menu</h2>
        <table>
          <tr>
            <th>Name</th>
            <th>Price</th>
            <th>Description</th>
            <th>Calories</th>
          </tr>

          <xsl:for-each select="food">
            <tr>
              <td><xsl:value-of select="name"/></td>

              <td>
                <xsl:choose>
                  <xsl:when test="price/@xlink:href">
                    <a href="{price/@xlink:href}">
                      <xsl:value-of select="price"/>
                    </a>
                  </xsl:when>
                  <xsl:otherwise>
                    <xsl:value-of select="price"/>
                  </xsl:otherwise>
                </xsl:choose>
              </td>

              <td>
                <xsl:choose>
                  <xsl:when test="description/@xlink:href">
                    <a href="{description/@xlink:href}">
                      <xsl:value-of select="description"/>
                    </a>
                  </xsl:when>
                  <xsl:otherwise>
                    <xsl:value-of select="description"/>
                  </xsl:otherwise>
                </xsl:choose>
              </td>

              <td><xsl:value-of select="calories"/></td>
            </tr>
          </xsl:for-each>
        </table>
      </body>
    </html>
  </xsl:template>

</xsl:stylesheet>



<!--
<?xml version="1.0" encoding="UTF-8"?>
<html xsl:version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<body style="font-family:Arial;font-size:12pt;background-color:#EEEEEE">
<xsl:for-each select="breakfast_menu/food">
  <div style="background-color:teal;color:white;padding:4px">
    <span style="font-weight:bold"><xsl:value-of select="name"/> - </span>
    <xsl:value-of select="price"/>
    </div>
  <div style="margin-left:20px;margin-bottom:1em;font-size:10pt">
    <p>
    <xsl:value-of select="description"/>
    <span style="font-style:italic"> (<xsl:value-of select="calories"/> calories per serving)</span>
    </p>
  </div>
</xsl:for-each>
</body>
</html>
-->