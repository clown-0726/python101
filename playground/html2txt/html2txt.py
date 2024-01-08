from selectolax.parser import HTMLParser

target_html = '''
<DOCUMENT>
<TYPE>424B5
<SEQUENCE>1
<FILENAME>d326517d424b5.htm
<DESCRIPTION>424B5
<TEXT>
<HTML><HEAD>
<TITLE>424B5</TITLE>
</HEAD>
 <BODY BGCOLOR="WHITE">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="right"><B>Filed Pursuant to Rule 424(b)(5) </B></P>
<P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="right"><B>Registration Statement <FONT STYLE="white-space:nowrap">No.&nbsp;333-248776</FONT> </B></P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center"><B>CALCULATION OF REGISTRATION FEE </B></P> <P STYLE="font-size:12pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE CELLSPACING="0" CELLPADDING="0" WIDTH="92%" BORDER="0" STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" ALIGN="center">


<TR>

<TD WIDTH="44%"></TD>

<TD VALIGN="bottom" WIDTH="4%"></TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TD VALIGN="bottom" WIDTH="4%"></TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TD VALIGN="bottom" WIDTH="3%"></TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TD VALIGN="bottom" WIDTH="4%"></TD>
<TD></TD>
<TD></TD>
<TD></TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:8pt">
<TD VALIGN="bottom" NOWRAP> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-bottom:1.00pt solid #000000; display:table-cell; font-size:8pt; font-family:Times New Roman; "><B>Title of Each Class&nbsp;of<BR>Securities to be
Registered</B></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="bottom" COLSPAN="2" ALIGN="center" STYLE="border-bottom:1.00pt solid #000000"><B>Amount to be<BR>Registered</B></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="bottom" COLSPAN="2" ALIGN="center" STYLE="border-bottom:1.00pt solid #000000"><B>Maximum<BR>Offering<BR>Price per<BR>Note</B></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom" COLSPAN="2" ALIGN="center" STYLE="border-bottom:1.00pt solid #000000"><B>Maximum<BR>Aggregate<BR>Offering Price</B></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="bottom" COLSPAN="2" ALIGN="center" STYLE="border-bottom:1.00pt solid #000000"><B>Amount of<BR>Registration<BR>Fee<SUP STYLE="font-size:85%; vertical-align:top">(1)(2)</SUP></B></TD>
<TD VALIGN="bottom">&nbsp;</TD></TR>


<TR BGCOLOR="#cceeff" STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">0.950% Senior Notes due 2024</P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">500,000,000</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">99.946</TD>
<TD NOWRAP VALIGN="bottom">%&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">499,730,000</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">54,520.55</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">2.350% Senior Notes due 2032</P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">500,000,000</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">99.939</TD>
<TD NOWRAP VALIGN="bottom">%&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">499,695,000</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">54,516.73</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR BGCOLOR="#cceeff" STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">3.050% Senior Notes due 2041</P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">500,000,000</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">99.480</TD>
<TD NOWRAP VALIGN="bottom">%&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">497,400,000</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">54,266.34</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:3.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><B>Total</B></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="bottom"></TD>
<TD VALIGN="bottom"></TD>
<TD VALIGN="bottom"></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="bottom"></TD>
<TD VALIGN="bottom"></TD>
<TD VALIGN="bottom"></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom"></TD>
<TD VALIGN="bottom"></TD>
<TD VALIGN="bottom"></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="bottom"><B>$</B></TD>
<TD VALIGN="bottom" ALIGN="right"><B>163,303.62</B></TD>
<TD NOWRAP VALIGN="bottom"><B>&nbsp;</B></TD></TR>
</TABLE> <P STYLE="line-height:8.0pt;margin-top:0pt;margin-bottom:2pt;border-bottom:1px solid #000000;width:11%">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%" VALIGN="top" ALIGN="left">(1)</TD>
<TD ALIGN="left" VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman; " ALIGN="left">The filing fee is calculated in accordance with Rule 457(r) of the Securities Act of 1933, as amended.
</P></TD></TR></TABLE>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%" VALIGN="top" ALIGN="left">(2)</TD>
<TD ALIGN="left" VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman; " ALIGN="left">This &#147;Calculation of Registration Fee&#148; table shall be deemed to update the &#147;Calculation of
Registration Fee&#148; table in Quanta Services, Inc.&#146;s Registration Statement on Form <FONT STYLE="white-space:nowrap">S-3</FONT> (File <FONT STYLE="white-space:nowrap">No.&nbsp;333-248776)</FONT> in accordance with Rules 456(b) and 457(r)
under the Securities Act of 1933, as amended. </P></TD></TR></TABLE>
</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"> </P> <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P>
<P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:8pt; font-family:Times New Roman"><B>PROSPECTUS SUPPLEMENT </B></P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:8pt; font-family:Times New Roman">(To prospectus dated
September&nbsp;14, 2020) </P> <P STYLE="margin-top:4pt; margin-bottom:0pt; font-size:12pt; font-family:Times New Roman" ALIGN="center"><B>$1,500,000,000 </B></P> <P STYLE="font-size:4pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<P STYLE="margin-top:0pt;margin-bottom:0pt" ALIGN="center">


<IMG SRC="https://ot-cdn.s3.us-west-2.amazonaws.com/filing/Archives/edgar/data/1050915/000119312521271415/g326517g12n84.jpg" ALT="LOGO">
 </P> <P STYLE="margin-top:4pt; margin-bottom:0pt; font-size:18pt; font-family:Times New Roman" ALIGN="center"><B>Quanta Services, Inc. </B></P>
<P STYLE="margin-top:4pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center"><B>$500,000,000 0.950% Senior Notes due 2024 </B></P>
<P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center"><B>$500,000,000 2.350% Senior Notes due 2032 </B></P>
<P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center"><B>$500,000,000 3.050% Senior Notes due 2041 </B></P> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P><center>
<P STYLE="line-height:6.0pt;margin-top:0pt;margin-bottom:2pt;border-bottom:1.00pt solid #000000;width:21%">&nbsp;</P></center> <P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:8pt; font-family:Times New Roman">We are offering
$500,000,000 aggregate principal amount of our 0.950% Senior Notes due 2024 (the &#147;2024 notes&#148;), $500,000,000 aggregate principal amount of our 2.350% Senior Notes due 2032 (the &#147;2032 notes&#148;) and $500,000,000 aggregate principal
amount of our 3.050% Senior Notes due 2041 (the &#147;2041 notes&#148; and, together with the 2024 notes and the 2032 notes, the &#147;notes&#148;). The 2024 notes will mature on October 1, 2024, the 2032 notes will mature on January 15, 2032 and
the 2041 notes will mature on October 1, 2041. We will pay interest on the 2024 notes semi-annually in arrears on April 1 and October 1 of each year, commencing April 1, 2022. We will pay interest on the 2032 notes semi-annually in arrears on
January 15 and July 15 of each year, commencing July 15, 2022. We will pay interest on the 2041 notes semi-annually in arrears on April 1 and October 1 of each year, commencing April 1, 2022. </P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:8pt; font-family:Times New Roman">The notes will be our senior unsecured obligations and will rank equally in right of payment with our existing and future senior unsecured
indebtedness. The notes will be effectively junior to our existing and future secured indebtedness to the extent of the value of the assets securing such indebtedness. The notes will not be guaranteed by any of our subsidiaries and will therefore be
structurally subordinated to all of the existing and future indebtedness and other liabilities of our subsidiaries, including trade payables. </P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:8pt; font-family:Times New Roman">We may redeem all or a portion of the notes at our option at any time or from time to time at the applicable redemption price in the
circumstances described in this prospectus supplement. See &#147;Description of Notes&#151;Optional Redemption.&#148; </P> <P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:8pt; font-family:Times New Roman">In the event that (x)
the Blattner Acquisition (as defined herein) is not consummated on or prior to June 30, 2022 or (y) the Merger Agreement (as defined herein) is terminated without the Blattner Acquisition being consummated, we will be required to redeem all of the
outstanding 2024 notes, 2032 notes and 2041 notes at a redemption price equal to 101% of the aggregate principal amount of the 2024 notes, 2032 notes and 2041 notes, respectively, plus accrued and unpaid interest, if any, to, but excluding, the
redemption date. See &#147;Description of Notes&#151;Special&nbsp;Mandatory&nbsp;Redemption.&#148; </P> <P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:8pt; font-family:Times New Roman">We will be required to offer to purchase
the notes upon the occurrence of a &#147;Change of Control Triggering Event&#148; (as defined herein) at a price equal to 101% of the principal amount of the notes to be repurchased, plus accrued and unpaid interest, if any, to, but excluding, the
date of purchase. See &#147;Description of Notes&#151;Purchase upon a Change of Control Triggering Event.&#148; </P> <P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:9pt; font-family:Times New Roman"><B>Neither the Securities
and Exchange Commission nor any state securities commission has approved or disapproved of these securities or determined if this prospectus supplement or the accompanying prospectus is truthful or complete. Any representation to the contrary is a
criminal offense. </B></P> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE CELLSPACING="0" CELLPADDING="0" WIDTH="100%" BORDER="0" STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:8pt" ALIGN="center">


<TR>

<TD WIDTH="49%"></TD>

<TD VALIGN="bottom" WIDTH="2%"></TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TD VALIGN="bottom" WIDTH="2%"></TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TD VALIGN="bottom" WIDTH="2%"></TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TD VALIGN="bottom" WIDTH="2%"></TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TD VALIGN="bottom" WIDTH="2%"></TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TD VALIGN="bottom" WIDTH="2%"></TD>
<TD></TD>
<TD></TD>
<TD></TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:7pt">
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="bottom" COLSPAN="2" ALIGN="center" STYLE="border-bottom:1.00pt solid #000000"><B>Per<BR>2024&nbsp;Note</B></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom" COLSPAN="2" ALIGN="center" STYLE="border-bottom:1.00pt solid #000000"><B>Total</B><br><B>2024&nbsp;Notes</B></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="bottom" COLSPAN="2" ALIGN="center" STYLE="border-bottom:1.00pt solid #000000"><B>Per<BR>2032&nbsp;Note</B></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom" COLSPAN="2" ALIGN="center" STYLE="border-bottom:1.00pt solid #000000"><B>Total</B><br><B>2032&nbsp;Notes</B></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="bottom" COLSPAN="2" ALIGN="center" STYLE="border-bottom:1.00pt solid #000000"><B>Per<BR>2041&nbsp;Note</B></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom" COLSPAN="2" ALIGN="center" STYLE="border-bottom:1.00pt solid #000000"><B>Total</B><br><B>2041&nbsp;Notes</B></TD>
<TD VALIGN="bottom">&nbsp;</TD></TR>


<TR BGCOLOR="#cceeff" STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:8pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:8pt; font-family:Times New Roman">Public offering price (1)</P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">99.946</TD>
<TD NOWRAP VALIGN="bottom">%&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">499,730,000</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">99.939</TD>
<TD NOWRAP VALIGN="bottom">%&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">499,695,000</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">99.480</TD>
<TD NOWRAP VALIGN="bottom">%&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">497,400,000</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:8pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:8pt; font-family:Times New Roman">Underwriting discount</P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">0.350</TD>
<TD NOWRAP VALIGN="bottom">%&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">1,750,000</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">0.650</TD>
<TD NOWRAP VALIGN="bottom">%&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">3,250,000</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">0.875</TD>
<TD NOWRAP VALIGN="bottom">%&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">4,375,000</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR BGCOLOR="#cceeff" STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:8pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:8pt; font-family:Times New Roman">Proceeds, before expenses, to us (1)</P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">99.596</TD>
<TD NOWRAP VALIGN="bottom">%&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">497,980,000</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">99.289</TD>
<TD NOWRAP VALIGN="bottom">%&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">496,445,000</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">98.605</TD>
<TD NOWRAP VALIGN="bottom">%&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">493,025,000</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
</TABLE> <P STYLE="line-height:8.0pt;margin-top:0pt;margin-bottom:2pt;border-bottom:1px solid #000000;width:11%">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:8pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%" VALIGN="top" ALIGN="left">(1)</TD>
<TD ALIGN="left" VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; font-size:8pt; font-family:Times New Roman; " ALIGN="left">Plus accrued interest, if any, from September 23, 2021, if settlement occurs after that date.
</P></TD></TR></TABLE> <P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:8pt; font-family:Times New Roman">The notes are new issues of securities with no established trading market. We do not intend to apply for listing of the
notes on any securities exchange or for inclusion of the notes on any automated dealer quotation system. We expect that delivery of the notes, in book-entry form only through the facilities of The Depository Trust Company for the accounts of its
participants, including Euroclear Bank SA/NV, as operator of the Euroclear System, and Clearstream Banking, S.A., will be made on or about September 23, 2021. </P> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P><center>
<P STYLE="line-height:6.0pt;margin-top:0pt;margin-bottom:2pt;border-bottom:1.00pt solid #000000;width:21%">&nbsp;</P></center> <P STYLE="margin-top:6pt; margin-bottom:0pt; font-size:8pt; font-family:Times New Roman" ALIGN="center"><I>Joint
Book-Running Managers </I></P> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE CELLSPACING="0" CELLPADDING="0" WIDTH="100%" BORDER="0" STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" ALIGN="center">


<TR>

<TD WIDTH="50%"></TD>

<TD VALIGN="bottom" WIDTH="1%"></TD>
<TD WIDTH="48%"></TD></TR>


<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top" ALIGN="center"><B>BofA Securities</B></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom" NOWRAP ALIGN="center"><B>Wells Fargo Securities</B></TD></TR>
</TABLE>
<TABLE CELLSPACING="0" CELLPADDING="0" WIDTH="100%" BORDER="0" STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" ALIGN="center">


<TR>

<TD WIDTH="34%"></TD>

<TD VALIGN="bottom"></TD>
<TD WIDTH="32%"></TD>

<TD VALIGN="bottom" WIDTH="1%"></TD>
<TD WIDTH="32%"></TD></TR>


<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top" ALIGN="center"><B>J.P. Morgan</B></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom" NOWRAP ALIGN="center"><B>PNC Capital Markets LLC</B></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom" NOWRAP ALIGN="center"><B>Truist Securities</B></TD></TR>
</TABLE> <P STYLE="margin-top:6pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center"><I>Senior Co-Managers </I></P> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE CELLSPACING="0" CELLPADDING="0" WIDTH="100%" BORDER="0" STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" ALIGN="center">


<TR>

<TD WIDTH="34%"></TD>

<TD VALIGN="bottom"></TD>
<TD WIDTH="32%"></TD>

<TD VALIGN="bottom" WIDTH="1%"></TD>
<TD WIDTH="32%"></TD></TR>


<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top" ALIGN="center"><B>BBVA</B></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom" NOWRAP ALIGN="center"><B>BMO Capital Markets</B></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom" NOWRAP ALIGN="center"><B>BNP PARIBAS</B></TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top" ALIGN="center"><B>Citizens Capital Markets</B></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom"></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom" NOWRAP ALIGN="center"><B>MUFG</B></TD></TR>
</TABLE> <P STYLE="margin-top:6pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center"><I>Co-Managers </I></P> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE CELLSPACING="0" CELLPADDING="0" WIDTH="100%" BORDER="0" STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" ALIGN="center">


<TR>

<TD WIDTH="50%"></TD>

<TD VALIGN="bottom" WIDTH="1%"></TD>
<TD WIDTH="49%"></TD></TR>


<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top" ALIGN="center"><B>HSBC</B></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom" NOWRAP ALIGN="center"><B>US Bancorp </B></TD></TR>
</TABLE> <P STYLE="margin-top:6pt; margin-bottom:0pt; font-size:8pt; font-family:Times New Roman" ALIGN="center"><B>The date of this prospectus supplement is September 9, 2021 </B></P>
</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman"><B>Neither we nor the underwriters have authorized anyone to provide you with any
information other than the information contained in, or incorporated by reference in, this prospectus supplement, the accompanying base prospectus and any free writing prospectus prepared by or on behalf of us. We and the underwriters take no
responsibility for, and can provide no assurance as to the reliability of, any other information that others may give you. This prospectus supplement may be used only for the purpose for which it has been prepared. </B></P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman"><B>We are not, and the underwriters are not, making an offer to sell these securities in any jurisdiction where the offer or sale is not
permitted. You should not assume that the information appearing in this prospectus supplement, the accompanying prospectus or any document incorporated by reference is accurate as of any date other than the date of the applicable document. Our
business, financial condition, results of operations and prospects may have changed since the relevant date. Neither this prospectus supplement nor the accompanying prospectus constitutes an offer or an invitation on our behalf or on behalf of the
underwriters to subscribe for or purchase any of the securities, and may not be used for or in connection with an offer or solicitation by anyone, in any jurisdiction in which such an offer or solicitation is not authorized or to any person to whom
it is unlawful to make such an offer or solicitation. </B></P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">We expect that delivery of the notes will be made to investors on or about
September 23, 2021, which will be the tenth business day following the date of this prospectus supplement (such settlement being referred to as &#147;T+10&#148;). Under Rule <FONT STYLE="white-space:nowrap">15c6-1</FONT> under the Securities
Exchange Act of 1934, as amended (the &#147;Exchange Act&#148;), trades in the secondary market are required to settle in two business days, unless the parties to any such trade expressly agree otherwise. Accordingly, purchasers who wish to trade
notes prior to the second business day before the delivery of the notes hereunder will be required, by virtue of the fact that the notes initially settle in T+10, to specify an alternate settlement arrangement at the time of any such trade to
prevent a failed settlement. Purchasers of the notes who wish to trade the notes prior to their date of delivery hereunder should consult their advisors. </P>
</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center"><B><A NAME="toc"></A>TABLE OF CONTENTS </B></P>
<P STYLE="font-size:12pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE CELLSPACING="0" CELLPADDING="0" WIDTH="100%" BORDER="0" STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" ALIGN="center">


<TR>

<TD WIDTH="95%"></TD>

<TD VALIGN="bottom" WIDTH="1%"></TD>
<TD></TD>
<TD></TD>
<TD></TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:8pt">
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="bottom" COLSPAN="2" ALIGN="center" STYLE="border-bottom:1.00pt solid #000000"><B>Page</B></TD>
<TD VALIGN="bottom">&nbsp;</TD></TR>


<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><A HREF="#supprom326517_1">CAUTIONARY STATEMENT REGARDING FORWARD-LOOKING STATEMENTS</A></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">i</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><A HREF="#supprom326517_2">ABOUT THIS PROSPECTUS SUPPLEMENT</A></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">v</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><A HREF="#supprom326517_3">INCORPORATION OF CERTAIN INFORMATION BY REFERENCE</A></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">v</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><A HREF="#supprom326517_4">SUMMARY</A></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right"><FONT STYLE="white-space:nowrap">S-1</FONT></TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><A HREF="#supprom326517_5">RISK FACTORS</A></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right"><FONT STYLE="white-space:nowrap">S-11</FONT></TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><A HREF="#supprom326517_6">USE OF PROCEEDS</A></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right"><FONT STYLE="white-space:nowrap">S-20</FONT></TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><A HREF="#supprom326517_7">CAPITALIZATION</A></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right"><FONT STYLE="white-space:nowrap">S-21</FONT></TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><A HREF="#supprom326517_8">DESCRIPTION OF NOTES</A></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right"><FONT STYLE="white-space:nowrap">S-23</FONT></TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><A HREF="#supprom326517_9">MATERIAL U.S. FEDERAL INCOME TAX CONSEQUENCES</A></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right"><FONT STYLE="white-space:nowrap">S-40</FONT></TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><A HREF="#supprom326517_10">UNDERWRITING (CONFLICTS OF INTEREST)</A></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right"><FONT STYLE="white-space:nowrap">S-46</FONT></TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><A HREF="#supprom326517_11">LEGAL MATTERS</A></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right"><FONT STYLE="white-space:nowrap">S-53</FONT></TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><A HREF="#supprom326517_12">EXPERTS</A></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right"><FONT STYLE="white-space:nowrap">S-53</FONT></TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
</TABLE> <P STYLE="font-size:12pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE CELLSPACING="0" CELLPADDING="0" WIDTH="100%" BORDER="0" STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" ALIGN="center">


<TR>

<TD WIDTH="97%"></TD>

<TD VALIGN="bottom" WIDTH="1%"></TD>
<TD></TD>
<TD></TD>
<TD></TD></TR>


<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><A HREF="#toc326517_1">ABOUT THIS PROSPECTUS</A></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">i</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><A HREF="#toc326517_2">ABOUT QUANTA SERVICES, INC.</A></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">1</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><A HREF="#toc326517_3">RISK FACTORS</A></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">2</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><A HREF="#toc326517_4">FORWARD-LOOKING STATEMENTS</A></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">3</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><A HREF="#toc326517_5">USE OF PROCEEDS</A></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">7</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><A HREF="#toc326517_6">DESCRIPTION OF CAPITAL STOCK</A></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">8</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><A HREF="#toc326517_7">DESCRIPTION OF DEBT SECURITIES</A></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">12</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><A HREF="#toc326517_8">DESCRIPTION OF WARRANTS</A></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">23</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><A HREF="#toc326517_9">DESCRIPTION OF DEPOSITARY SHARES</A></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">24</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><A HREF="#toc326517_10">DESCRIPTION OF PURCHASE CONTRACTS AND PURCHASE UNITS</A></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">25</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><A HREF="#toc326517_11">DESCRIPTION OF UNITS</A></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">26</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><A HREF="#toc326517_12">PLAN OF DISTRIBUTION</A></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">27</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><A HREF="#toc326517_13">LEGAL MATTERS</A></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">30</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><A HREF="#toc326517_14">EXPERTS</A></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">30</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><A HREF="#toc326517_15">WHERE YOU CAN FIND MORE INFORMATION</A></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">30</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><A HREF="#toc326517_16">INCORPORATION OF CERTAIN INFORMATION BY REFERENCE</A></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">30</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
</TABLE>
</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center"><B><A NAME="supprom326517_1"></A>CAUTIONARY STATEMENT REGARDING FORWARD-LOOKING STATEMENTS
</B></P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Quanta is including this Cautionary Statement Regarding Forward-Looking Statements reflecting assumptions, expectations, projections,
intentions or beliefs about future events that are intended to caution investors and qualify for the &#147;safe harbor&#148; from liability established by the Private Securities Litigation Reform Act of 1995 (the &#147;Act&#148;) for forward-looking
statements.. You can identify these forward-looking statements by the fact that they do not relate strictly to historical or current facts. They use words such as &#147;anticipate,&#148; &#147;estimate,&#148; &#147;project,&#148;
&#147;forecast,&#148; &#147;may,&#148; &#147;will,&#148; &#147;should,&#148; &#147;could,&#148; &#147;expect,&#148; &#147;believe,&#148; &#147;plan,&#148; &#147;intend&#148; and other words of similar meaning. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">In particular, these include, but are not limited to, statements relating to the following: </P>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">projected revenues, net income, earnings per share, margins, cash flows, liquidity, weighted average shares
outstanding, capital expenditures and tax rates, as well as other projections of operating or financial results; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">expectations regarding our or Blattner&#146;s (as defined herein) business or financial outlook;
</P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">expectations regarding opportunities, technological developments, competitive positioning, future economic and
regulatory conditions and other trends in particular markets or industries; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">expectations regarding the pandemic associated with the novel coronavirus disease that began in 2019 <FONT
STYLE="white-space:nowrap">(&#147;COVID-19&#148;),</FONT> including the continued and potential impact of the <FONT STYLE="white-space:nowrap">COVID-19</FONT> pandemic and of governmental responses to the pandemic on our business, operations, supply
chain, personnel, financial condition, results of operations, cash flows and liquidity; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">expectations regarding our plans and strategies; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the business plans or financial condition of our or Blattner&#146;s customers, including with respect to the <FONT
STYLE="white-space:nowrap">COVID-19</FONT> pandemic and the transition to a carbon-neutral economy; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the potential impact of commodity prices and production volumes on our business, financial condition, results of
operations, cash flows and demand for our services; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the potential benefits from, and future financial and operational performance of, acquired businesses and our
investments, including the Blattner Acquisition; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">beliefs and assumptions about the collectability of receivables; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the expected value of contracts or intended contracts with customers, as well as the scope, services, term or
results of any awarded or expected projects; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the development of and opportunities with respect to future projects, including renewable energy projects and
larger electric transmission and pipeline projects; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">future capital allocation initiatives, including the amount and timing of, and strategies with respect to, any
future stock repurchases and expectations regarding the declaration, amount and timing of any future cash dividends; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the impact of existing or potential legislation or regulation; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">potential opportunities that may be indicated by bidding activity or similar discussions with customers;
</P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the future demand for and availability of labor resources in the industries we serve; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the expected realization of our or Blattner&#146;s remaining performance obligations or backlog;
</P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the expected outcome of pending or threatened legal proceedings; and </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">possible recovery of pending or contemplated insurance claims, change orders and claims asserted against
customers or third parties. </P></TD></TR></TABLE>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">i </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">These forward-looking statements are not guarantees of future performance, involve or rely
on a number of risks, uncertainties, and assumptions that are difficult to predict or are beyond our control, and reflect management&#146;s beliefs and assumptions based on information available at the time the statements are made. We caution you
that actual outcomes and results may differ materially from what is expressed, implied or forecasted by our forward-looking statements and that any or all of our forward-looking statements may turn out to be inaccurate or incorrect. These statements
can be affected by inaccurate assumptions and by known or unknown risks and uncertainties, including the following: </P> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">market, industry, economic, financial or political conditions that are outside of our control, including
economic, energy, infrastructure and environmental policies and plans that are adopted or proposed by the U.S. federal and state governments or other governments in territories or countries in which we operate, weakness in the capital markets and
the ongoing and potential impact on financial markets and worldwide economic activity of the <FONT STYLE="white-space:nowrap">COVID-19</FONT> pandemic and governmental responses thereto; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">quarterly variations in our operating and financial results, liquidity, financial condition, cash flows, capital
requirements, and reinvestment opportunities, including the ongoing and potential impact to our business, operations and supply chains resulting from the <FONT STYLE="white-space:nowrap">COVID-19</FONT> pandemic and governmental responses thereto;
</P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the severity, magnitude and duration of the <FONT STYLE="white-space:nowrap">COVID-19</FONT> pandemic, including
impacts of the pandemic and of business and governmental responses thereto on our operations, personnel and supply chains, and on commercial activity and demand across our business and our customers&#146; businesses, as well as our inability to
predict the extent to which the <FONT STYLE="white-space:nowrap">COVID-19</FONT> pandemic will adversely impact our business, financial performance, results of operations, financial position, liquidity, cash flows, the price of our securities and
the achievement of our strategic objectives; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">trends and growth opportunities in relevant markets, including our or Blattner&#146;s ability to obtain future
project awards; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the time and costs required to exit and resolve outstanding matters related to our Latin American operations, as
well as the business and political climate in Latin America; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">delays, deferrals, reductions in scope or cancellations of anticipated, pending or existing projects as a result
of, among other things, the <FONT STYLE="white-space:nowrap">COVID-19</FONT> pandemic, weather, regulatory or permitting issues, environmental processes, project performance issues, claimed force majeure events, protests or other political activity,
legal challenges, reductions or eliminations in governmental funding or customer capital constraints; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the effect of commodity prices and commodity production volumes on our operations and growth opportunities and on
our customers&#146; capital programs and demand for our services; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the successful negotiation, execution, performance and completion of anticipated, pending and existing contracts;
</P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">risks associated with operational hazards that arise due to the nature of the services we provide and the
conditions in which we operate, including, among others, wildfires and explosions; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">unexpected costs, liabilities, fines or penalties that may arise from legal proceedings, indemnity obligations,
reimbursement obligations associated with letters of credit or bonds, multiemployer pension plans (e.g., underfunding of liabilities, termination or withdrawal liability) or other claims or actions asserted against us, including amounts that are not
covered by, or are in excess of the coverage under, our third-party insurance; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">potential unavailability or cancellation of third-party insurance coverage, as well as the exclusion of coverage
for certain losses, potential increases in premiums for coverage deemed beneficial to us, or the unavailability of coverage deemed beneficial to us at reasonable and competitive rates (e.g., coverage for wildfire events); </P></TD></TR></TABLE>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">ii </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">

<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">damage to our brands or reputation arising as a result of cyber-security breaches, environmental and occupational
health and safety matters, corporate scandal, failure to successfully perform a high-profile project, involvement in a catastrophic event (e.g., fire, explosion) or other negative incidents; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">disruptions in, or failure to adequately protect, our information technology systems; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">our dependence on suppliers, subcontractors, equipment manufacturers and other third parties and the impact of
the <FONT STYLE="white-space:nowrap">COVID-19</FONT> pandemic on these service providers; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">estimates and assumptions related to our financial results, remaining performance obligations and backlog;
</P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">our ability to attract and the potential shortage of skilled employees, as well as our ability to retain key
personnel and qualified employees; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">our dependence on fixed price contracts and the potential that we incur losses with respect to these contracts,
including as a result of inaccurate estimates of project costs or inability to meet project schedule requirements or achieve guaranteed performance or quality standards for a project; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">adverse weather conditions, natural disasters and other emergencies, including wildfires, pandemics (including
the ongoing <FONT STYLE="white-space:nowrap">COVID-19</FONT> pandemic), hurricanes, tropical storms, floods, earthquakes and other geological- and weather-related hazards; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">our ability to generate internal growth; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">competition in our business, including our ability to effectively compete for new projects and market share;
</P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the future development of natural resources; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the failure of existing or potential legislative actions and initiatives to result in increased demand for our
services; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">fluctuations of prices of certain materials used in our and our customers&#146; businesses, including as a result
of inflation, the imposition of tariffs, governmental regulations affecting the sourcing of certain materials and equipment and other changes in U.S. trade relationships with foreign countries; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">cancellation provisions within our contracts and the risk that contracts expire and are not renewed or are
replaced on less favorable terms; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">loss of customers with whom we have long-standing or significant relationships; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the potential that our participation in joint ventures or similar structures exposes us to liability and/or harm
to our reputation as a result of acts or omissions by our partners; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">our inability or failure to comply with the terms of our contracts, which may result in additional costs,
unexcused delays, warranty claims, failure to meet performance guarantees, damages or contract terminations; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the inability or refusal of our customers or third-party contractors to pay for services, which could be
attributable to, among other things, the <FONT STYLE="white-space:nowrap">COVID-19</FONT> pandemic or challenged energy markets and which could result in our inability to collect our outstanding receivables, failure to recover amounts billed to, or
avoidance of certain payments received from, customers in bankruptcy or failure to recover on change orders or contract claims; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">budgetary or other constraints that may reduce or eliminate tax incentives or government funding for projects,
which may result in project delays or cancellations; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">our or Blattner&#146;s inability to successfully complete our remaining performance obligations or realize our
backlog; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">technological advancements and market developments that could reduce demand for our services;
</P></TD></TR></TABLE>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">iii </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">

<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">risks associated with operating in international markets, including instability of foreign governments, currency
exchange fluctuations, and compliance with unfamiliar foreign legal systems and cultural practices, the U.S. Foreign Corrupt Practices Act and other applicable anti-bribery and anti-corruption laws, and complex U.S. and foreign tax regulations and
international treaties; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">our inability to successfully identify, complete, integrate and realize synergies from acquisitions, including
the inability to retain key personnel from acquired businesses; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the potential adverse impact of acquisitions and investments, including the potential increase in risks already
existing in our operations and poor performance or decline in value of acquired businesses or investments; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the adverse impact of impairments of goodwill, other intangible assets, receivables, long-lived assets or
investments; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">difficulties arising from our decentralized management structure; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the impact of the unionized portion of our workforce on our operations, including labor stoppages or
interruptions due to strikes or lockouts; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the inability to access sufficient funding to finance desired growth and operations, including our ability to
access capital markets on favorable terms, as well as fluctuations in the price and trading volume of our common stock, debt covenant compliance, interest rate fluctuations and other factors affecting our financing and investing activities;
</P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">our ability to obtain bonds, letters of credit and other project security; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">risks related to the implementation of new information technology systems; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">new or changed tax laws, treaties or regulations; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">inability to realize deferred tax assets; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">significant fluctuations in foreign currency exchange rates; and </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the other risks and uncertainties discussed under &#147;Risk Factors&#148; in this prospectus supplement and the
accompanying prospectus and in our Annual Report on Form <FONT STYLE="white-space:nowrap">10-K</FONT> for the year ended December&nbsp;31, 2020, our Quarterly Report on Form <FONT STYLE="white-space:nowrap">10-Q</FONT> for the quarterly period ended
March&nbsp;31, 2021 and our Quarterly Report on Form <FONT STYLE="white-space:nowrap">10-Q</FONT> for the quarterly period ended June&nbsp;30, 2021. </P></TD></TR></TABLE>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">All of our forward-looking statements, whether written or oral, are expressly qualified by these cautionary statements and any other
cautionary statements that may accompany such forward-looking statements or that are otherwise included in this prospectus supplement. Although forward-looking statements reflect our good faith beliefs at the time they are made, reliance should not
be placed on forward-looking statements because they involve known and unknown risks, uncertainties and other factors, which may cause our actual results, performance or achievements to differ materially from anticipated future results, performance
or achievements expressed or implied by such forward-looking statements. In addition, we do not undertake and expressly disclaim any obligation to update or revise any forward-looking statements to reflect events or circumstances after the date of
this prospectus supplement or otherwise. </P>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">iv </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center"><B><A NAME="supprom326517_2"></A>ABOUT THIS PROSPECTUS SUPPLEMENT </B></P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">This document is in two parts. The first part is the prospectus supplement, which describes the specific terms of the notes we are offering
and certain other matters relating to us and our financial condition. The second part, the accompanying prospectus, gives more general information about securities we may offer from time to time, some of which may not apply to the notes we are
offering. You should read this prospectus supplement along with the accompanying prospectus, as well as the documents incorporated by reference. If the description of the offering varies between this prospectus supplement and the accompanying
prospectus, you should rely on the information in this prospectus supplement. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">In this prospectus supplement and the accompanying
prospectus, except under the headings &#147;Description of Notes&#148; in this prospectus supplement, references to &#147;Quanta,&#148; &#147;we,&#148; &#147;us,&#148; and &#147;our&#148; refer to Quanta Services, Inc. and its consolidated
subsidiaries, unless the context indicates otherwise, and references to our &#147;revolving credit facility&#148; refer to our revolving credit facility under our existing credit agreement (after giving effect to the credit agreement amendment) as
described in &#147;Summary&#151;Recent Developments&#151;Credit Agreement Amendment,&#148; unless the context indicates otherwise. </P> <P STYLE="margin-top:24pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center"><B><A NAME="supprom326517_3">
</A>INCORPORATION OF CERTAIN INFORMATION BY REFERENCE </B></P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The Securities and Exchange Commission (the &#147;SEC&#148;) allows us to
incorporate by reference certain information filed with the SEC, which means that we can disclose important information to you by referring you to those documents. The information we incorporate by reference is an important part of this prospectus
supplement, and later information that Quanta files with the SEC will automatically update and supersede the information in this prospectus supplement. We incorporate by reference the documents listed below (and any amendments to these documents)
that have been previously filed with the SEC and any future filings Quanta makes with the SEC under Sections 13(a), 13(c), 14 or 15(d) of the Exchange Act (excluding any information furnished under Items 2.02 or 7.01 and exhibits related to such
Items in any Current Report on Form <FONT STYLE="white-space:nowrap">8-K),</FONT> until the termination of this offering. We are not, however, incorporating by reference any future filings or any documents or portions thereof contained in future
filings that are not deemed &#147;filed&#148; with the SEC. </P> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">our Annual Report on <A HREF="http://www.sec.gov/Archives/edgar/data/../../../ix?doc=/Archives/edgar/data/1050915/000105091521000009/pwr-20201231.htm">Form
 <FONT STYLE="white-space:nowrap">10-K</FONT></A> for the year ended December&nbsp;31, 2020, filed with the SEC on March&nbsp;1, 2021 (the &#147;2020 Annual Report&#148;); </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">our Quarterly Report on <A HREF="http://www.sec.gov/Archives/edgar/data/../../../ix?doc=/Archives/edgar/data/1050915/000105091521000072/pwr-20210331.htm">Form
 <FONT STYLE="white-space:nowrap">10-Q</FONT></A> for the quarterly period ended March&nbsp;31, 2021, filed with the SEC on May&nbsp;7, 2021; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">our Quarterly Report on <A HREF="http://www.sec.gov/Archives/edgar/data/../../../ix?doc=/Archives/edgar/data/1050915/000105091521000103/pwr-20210630.htm">Form
 <FONT STYLE="white-space:nowrap">10-Q</FONT></A> for the quarterly period ended June&nbsp;30, 2021, filed with the SEC on August&nbsp;6, 2021 (the &#147;Q2 Quarterly Report&#148;); </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">our Current Reports on Form <FONT STYLE="white-space:nowrap">8-K</FONT> filed with the SEC on <A HREF="http://www.sec.gov/Archives/edgar/data/../../../ix?doc=/Archives/edgar/data/1050915/000119312521005316/d835098d8k.htm">January&nbsp;8,
 2021</A>, <A HREF="http://www.sec.gov/Archives/edgar/data/../../../ix?doc=/Archives/edgar/data/1050915/000119312521082968/d159158d8k.htm">March&nbsp;
16, 2021</A>, <A HREF="http://www.sec.gov/Archives/edgar/data/../../../ix?doc=/Archives/edgar/data/1050915/000119312521100443/d145179d8k.htm">March&nbsp;
30, 2021</A>, <A HREF="http://www.sec.gov/Archives/edgar/data/../../../ix?doc=/Archives/edgar/data/1050915/000119312521179954/d23244d8k.htm">June&nbsp;
2, 2021</A>, <A HREF="http://www.sec.gov/Archives/edgar/data/../../../ix?doc=/Archives/edgar/data/1050915/000119312521216497/d159777d8k.htm">July&nbsp;
15, 2021</A> (Item 5.02 only) and <A HREF="http://www.sec.gov/Archives/edgar/data/../../../ix?doc=/Archives/edgar/data/1050915/000119312521266919/d211565d8k.htm">September 8, 2021</A> (Items 1.01 and 3.02 only); and </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">our Definitive Proxy Statement on <A HREF="http://www.sec.gov/Archives/edgar/data/1050915/000119312521118459/d38532ddef14a.htm">Schedule
 14A</A> for our 2021 Annual Meeting of Stockholders, filed with the SEC on April&nbsp;16, 2021, to the extent incorporated by reference in Part III of the 2020 Annual Report. </P></TD></TR></TABLE>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Each person, including any beneficial owner, to whom a copy of this prospectus supplement has been delivered, may obtain copies of the
documents we incorporate by reference by contacting us at the address indicated below or by viewing the SEC&#146;s website at www.sec.gov. We will provide, without charge, upon written or oral request, a copy of any and all of the documents that
have been or may be incorporated by reference, except that exhibits to such documents will not be provided unless they are specifically incorporated by reference into such documents. Requests for copies of these documents should be directed to: </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">Quanta Services, Inc. </P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">Attn:
Corporate Secretary </P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">2800 Post Oak Boulevard, Suite 2600 Houston, Texas 77056 </P>
<P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">(713) <FONT STYLE="white-space:nowrap">629-7600</FONT> </P>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">v </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">

<div style ="BORDER-BOTTOM:1.00pt solid #000000;BORDER-LEFT:1.00pt solid #000000;BORDER-RIGHT:1.00pt solid #000000;BORDER-TOP:1.00pt solid #000000;MARGIN-LEFT:0px; MARGIN-RIGHT:0px;max-width:100%"><div style="width:97%; margin-top:1.5%; margin-left:1.5%; margin-right:-1.25%">

 <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center"><B><A NAME="supprom326517_4"></A>SUMMARY </B></P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman"><I>This summary highlights certain information contained elsewhere or incorporated by reference in this prospectus supplement and the
accompanying prospectus. Because this is only a summary, it does not contain all of the information that is important to you. You should read this entire prospectus supplement and accompanying prospectus, as well as the documents incorporated by
reference herein, including the risk factors and the financial statements and related notes included elsewhere herein and therein, before making a decision with respect to an investment in the notes. We also urge you to read Quanta&#146;s public
filings with the SEC, as they provide additional information about Quanta that you may find important. </I></P> <P STYLE="margin-top:24pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center"><B>About Quanta Services, Inc.
</B></P> <P STYLE="margin-top:12pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B>Overview </B></P> <P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">We are a leading
provider of specialty contracting services, delivering comprehensive infrastructure solutions for the electric and gas utility, communications, pipeline and energy industries in the United States, Canada, Australia and select other international
markets. The performance of our business generally depends on our ability to obtain contracts with customers and to effectively deliver the services provided under those contracts. The services we provide include the design, engineering, new
construction, upgrade and repair and maintenance of infrastructure within each of the industries we serve, such as electric power transmission and distribution networks; substation facilities; communications and cable multi-system operator networks;
gas utility systems; and pipeline transmission systems and facilities. Our customers include many of the leading companies in the industries we serve, and we endeavour to develop and maintain strategic alliances and preferred service provider status
with our customers. Our services are typically provided pursuant to master service agreements, repair and maintenance contracts and fixed price and <FONT STYLE="white-space:nowrap">non-fixed</FONT> price new construction contracts. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">We report our results under two reportable segments: (1)&nbsp;Electric Power Infrastructure Solutions and (2)&nbsp;Underground Utility and
Infrastructure Solutions. This structure is generally focused on broad <FONT STYLE="white-space:nowrap">end-user</FONT> markets for our services. Included within the Electric Power Infrastructure Solutions segment are the results related to our
telecommunications infrastructure services. </P> <P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B>Recent Developments </B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B><I>Blattner Acquisition </I></B></P> <P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">On
September&nbsp;1, 2021, we entered into an Agreement and Plan of Merger (the &#147;Merger Agreement&#148;) with Blattner Holding Company (&#147;Blattner&#148;) and Blizzard Merger Sub, LLC (&#147;Merger Sub&#148;). The Merger Agreement provides for
the merger of Merger Sub with and into Blattner with Blattner surviving the merger as our wholly owned subsidiary (the &#147;Blattner Acquisition&#148;). Blattner provides complete engineering, procurement, project management and construction
services to utility and renewable energy developers in North America for wind, solar and energy storage projects. Blattner has completed or been awarded more than 300 wind projects (approximately 49 GW installed generating capacity), more than 90
solar projects (approximately 12 GW installed generating capacity) and 17 energy storage projects. Blattner generated full-year 2020 revenues and EBITDA of approximately $2.4&nbsp;billion and $291&nbsp;million, respectively. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The transaction consideration anticipated to be paid at closing will consist of approximately $2.36&nbsp;billion in cash, subject to a working
capital adjustment, and 3.3&nbsp;million shares of common stock of Quanta valued at $337.5&nbsp;million (such agreed value as of the execution of the Merger Agreement), for total consideration of approximately $2.7&nbsp;billion. Additionally,
pursuant to the terms of the Merger Agreement, Blattner shareholders will be eligible for additional consideration of up to $300&nbsp;million to the extent certain financial performance targets are achieved by the acquired business during a
designated post-acquisition period. We intend to partially fund the cash portion of the transaction consideration for the Blattner Acquisition with the net proceeds of this offering. See &#147;Use of Proceeds.&#148; </P>
</div><br clear="All"></div>

 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">S-1 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">

<div style ="BORDER-BOTTOM:1.00pt solid #000000;BORDER-LEFT:1.00pt solid #000000;BORDER-RIGHT:1.00pt solid #000000;BORDER-TOP:1.00pt solid #000000;MARGIN-LEFT:0px; MARGIN-RIGHT:0px;max-width:100%"><div style="width:97%; margin-top:1.5%; margin-left:1.5%; margin-right:-1.25%">

 <P STYLE="margin-top:0pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The Merger Agreement contains customary representations and warranties, covenants and
conditions to closing. We expect to close the Blattner Acquisition during the fourth quarter of 2021, subject to the satisfaction of customary closing conditions. This offering is not conditioned upon the consummation of the Blattner Acquisition.
However, if the Blattner Acquisition is not consummated prior to a Special Mandatory Redemption Event (as defined in &#147;Description of Notes&#148;), we will be required to redeem all of the notes then outstanding on the terms set forth in
&#147;Description of Notes&#151;Special Mandatory Redemption.&#148; </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The table below presents certain financial information for Blattner
provided to us by Blattner management (dollars in millions): </P> <P STYLE="font-size:12pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE CELLSPACING="0" CELLPADDING="0" WIDTH="76%" BORDER="0" STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" ALIGN="center">


<TR>

<TD WIDTH="78%"></TD>

<TD VALIGN="bottom" WIDTH="5%"></TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TD VALIGN="bottom" WIDTH="5%"></TD>
<TD></TD>
<TD></TD>
<TD></TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:8pt">
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="bottom" COLSPAN="6" ALIGN="center" STYLE="border-bottom:1.00pt solid #000000"><B>Year Ended<BR>December&nbsp;31,</B></TD>
<TD VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:8pt">
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="bottom" COLSPAN="2" ALIGN="center" STYLE="border-bottom:1.00pt solid #000000"><B>2019</B></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="bottom" COLSPAN="2" ALIGN="center" STYLE="border-bottom:1.00pt solid #000000"><B>2020</B></TD>
<TD VALIGN="bottom">&nbsp;</TD></TR>


<TR BGCOLOR="#cceeff" STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">Revenue</P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">1,781</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">2,376</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">Operating Income</P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">109</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">275</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR BGCOLOR="#cceeff" STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">Remaining Performance Obligations / Backlog</P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">1,287</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">1,914</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">EBITDA<SUP STYLE="font-size:85%; vertical-align:top">(a)</SUP></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">133</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">291</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR BGCOLOR="#cceeff" STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">Capital Expenditures</P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">19</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">46</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
</TABLE> <P STYLE="font-size:12pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%" VALIGN="top" ALIGN="left">(a)</TD>
<TD ALIGN="left" VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman; " ALIGN="left">Blattner defines EBITDA as net income before interest, income taxes, depreciation and amortization. This <FONT
STYLE="white-space:nowrap">non-GAAP</FONT> measure should not be considered as an alternative to GAAP measures, such as net income, and may be calculated differently from, and therefore may not be comparable to, similarly titled measures used by
other companies. EBITDA is utilized in this prospectus supplement to enable investors to evaluate the performance of Blattner excluding the effects of certain items that impact the comparability of operating results between reporting periods. This
measure should be used in addition to, and not in lieu of, results prepared in conformity with GAAP. The below table reconciles Blattner&#146;s EBITDA to its most directly comparable GAAP financial measure, net income, for the respective periods (in
millions): </P></TD></TR></TABLE> <P STYLE="font-size:12pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE CELLSPACING="0" CELLPADDING="0" WIDTH="76%" BORDER="0" STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" ALIGN="center">


<TR>

<TD WIDTH="82%"></TD>

<TD VALIGN="bottom" WIDTH="5%"></TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TD VALIGN="bottom" WIDTH="5%"></TD>
<TD></TD>
<TD></TD>
<TD></TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:8pt">
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="bottom" COLSPAN="6" ALIGN="center" STYLE="border-bottom:1.00pt solid #000000"><B>Year Ended<BR>December&nbsp;31,</B></TD>
<TD VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:8pt">
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="bottom" COLSPAN="2" ALIGN="center" STYLE="border-bottom:1.00pt solid #000000"><B>2019</B></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="bottom" COLSPAN="2" ALIGN="center" STYLE="border-bottom:1.00pt solid #000000"><B>2020</B></TD>
<TD VALIGN="bottom">&nbsp;</TD></TR>


<TR BGCOLOR="#cceeff" STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">Net income</P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">120</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">279</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">Interest expense</P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">1</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">1</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR BGCOLOR="#cceeff" STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">Interest income</P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">(3</TD>
<TD NOWRAP VALIGN="bottom">)&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">(5</TD>
<TD NOWRAP VALIGN="bottom">)&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">Income Taxes</P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">&#151;&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">&#151;&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR BGCOLOR="#cceeff" STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">Depreciation</P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">15</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">16</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">Amortization</P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">&#151;&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">&#151;&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="font-size:1px; ">
<TD VALIGN="bottom"></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD>&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD>&nbsp;</TD></TR>
<TR BGCOLOR="#cceeff" STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">EBITDA</P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">133</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">291</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="font-size:1px; ">
<TD VALIGN="bottom"></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:3.00px double #000000">&nbsp;</P></TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:3.00px double #000000">&nbsp;</P></TD>
<TD>&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:3.00px double #000000">&nbsp;</P></TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:3.00px double #000000">&nbsp;</P></TD>
<TD>&nbsp;</TD></TR>
</TABLE> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">PricewaterhouseCoopers LLP has not audited, reviewed, examined, compiled nor applied agreed-upon procedures
with respect to the financial and operational information related to the Blattner Acquisition and, accordingly, PricewaterhouseCoopers LLP does not express an opinion or any other form of assurance with respect thereto. The PricewaterhouseCoopers
LLP report incorporated by reference in this document relates to Quanta&#146;s previously issued financial statements. It does not extend to the financial and operational information related to the Blattner Acquisition and should not be read to do
so. Accordingly, you should not place undue reliance on this information. Because Blattner is a privately-held corporation, the financial information of Blattner presented herein may not give effect to new or revised accounting standards that are
required to be adopted by publicly-traded companies. See &#147;Risk Factors&#151;Risks Relating to the Blattner Acquisition&#151;We are not providing pro forma financial statements reflecting the impact of the Blattner Acquisition on our historical
financial information or separate historical financial statements of Blattner.&#148; </P>
</div><br clear="All"></div><br clear="All">

 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">S-2 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">

<div style ="BORDER-BOTTOM:1.00pt solid #000000;BORDER-LEFT:1.00pt solid #000000;BORDER-RIGHT:1.00pt solid #000000;BORDER-TOP:1.00pt solid #000000;MARGIN-LEFT:0px; MARGIN-RIGHT:0px;max-width:100%"><div style="width:97%; margin-top:1.5%; margin-left:1.5%; margin-right:-1.25%">

 <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B><I>Credit Agreement Amendment </I></B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Following the completion of this offering, we expect to enter into an amendment (the &#147;credit agreement amendment&#148;) to our existing
credit agreement with Bank of America, N.A., as administrative agent, and the lenders party thereto (the &#147;existing credit agreement&#148;). We expect the credit agreement amendment to, among other things, (i)&nbsp;provide for a new term loan
facility in an amount up to $750 million (our &#147;term loan facility&#148;), which we expect to use to partially finance the cash portion of the consideration for the Blattner Acquisition, (ii)&nbsp;provide that we may borrow up to a certain
amount under our revolving credit facility in order to partially finance the cash portion of the consideration for the Blattner Acquisition, subject to certain limited conditions precedent, and (iii)&nbsp;extend the maturity date from
September&nbsp;22, 2025 to the fifth anniversary of the effective date of the credit agreement amendment. The credit agreement amendment is being negotiated as of the date of this prospectus supplement and its effectiveness therefore remains subject
to market conditions and the satisfaction of certain conditions precedent, and there are no assurances that we will enter into the credit agreement amendment on the terms described herein, including with respect to the size of our term loan
facility, or at all; if we enter into the credit agreement amendment, we will not be obligated to make any borrowings thereunder. This offering is not conditioned on our entering into the credit agreement amendment. </P>
<P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B><I>Bridge Financing </I></B></P> <P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">In connection
with entering into the Merger Agreement, we entered into a commitment letter (the &#147;Commitment Letter&#148;), dated as of September&nbsp;1, 2021, with Bank of America, N.A., BofA Securities, Inc., Wells Fargo Bank, National Association and Wells
Fargo Securities, LLC (collectively, the &#147;Commitment Parties&#148;). Pursuant to the Commitment Letter, two of the Commitment Parties have committed to provide us with a <FONT STYLE="white-space:nowrap">364-day</FONT> senior unsecured bridge
facility in an aggregate principal amount of up to $2,183.5&nbsp;million (the &#147;Bridge Facility&#148;), subject to the terms and conditions set forth in the Commitment Letter. Although we do not currently expect to utilize the Bridge Facility,
the Bridge Facility will be available to us to finance the cash consideration estimated to be due at closing of the Blattner Acquisition and to pay fees and expenses incurred in connection therewith. The Commitment Letter provides that the
commitments under the Bridge Facility will be permanently reduced (and, in the event it is funded, the Bridge Facility must be prepaid) on a <FONT STYLE="white-space:nowrap"><FONT STYLE="white-space:nowrap">dollar-for-dollar</FONT></FONT> basis by,
among other sources, the net cash proceeds of this offering or, with certain limited exceptions, the net cash proceeds of other indebtedness for borrowed money incurred (other than indebtedness we incur under our existing credit facility, unless
such indebtedness is incurred for the purpose of financing the cash portion of the consideration for the Blattner Acquisition). In addition, but without duplication, the Commitment Letter provides that the commitments under the Bridge Facility will
be permanently reduced by 100% of the commitments pursuant to our term loan facility as long as the conditions to availability of our term loan facility are no more restrictive than the Bridge Facility. </P>
<P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B>Principal Executive Offices and Internet Address </B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Our principal executive offices are located at 2800 Post Oak Boulevard, Suite 2600, Houston, Texas&nbsp;77056, and our telephone number is
(713) <FONT STYLE="white-space:nowrap">629-7600.</FONT> Our website is located at www.quantaservices.com. We make available our periodic reports and other information filed with or furnished to the SEC free of charge through our website, as soon as
reasonably practicable after those reports and other information are electronically filed with or furnished to the SEC. Except for the documents expressly referenced above under &#147;Incorporation of Certain Information by Reference&#148; that are
also posted on our website, information contained on or accessible from our website or any other website is not incorporated by reference herein and does not constitute a part of this prospectus supplement. </P>
</div><br clear="All"></div>

 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">S-3 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">

<div style ="BORDER-BOTTOM:1.00pt solid #000000;BORDER-LEFT:1.00pt solid #000000;BORDER-RIGHT:1.00pt solid #000000;BORDER-TOP:1.00pt solid #000000;MARGIN-LEFT:0px; MARGIN-RIGHT:0px;max-width:100%"><div style="width:97%; margin-top:1.5%; margin-left:1.5%; margin-right:-1.25%">

 <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center"><B>The Offering </B></P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman"><I>The following summary contains basic information about the notes and is not intended to be complete. It does not contain all the
information that is important to you. For a more complete understanding of the notes, see &#147;Description of Notes.&#148; Capitalized terms not otherwise defined herein shall have the same meanings given them in the &#147;Description of
Notes&#148; section of this prospectus supplement. In the following summary, all references to &#147;Quanta,&#148; &#147;we,&#148; &#147;us&#148; and &#147;our&#148; refer only to Quanta Services, Inc. and not to any of its subsidiaries. </I></P>
<P STYLE="font-size:12pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE CELLSPACING="0" CELLPADDING="0" WIDTH="100%" BORDER="0" STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" ALIGN="center">


<TR>

<TD WIDTH="43%"></TD>

<TD VALIGN="bottom" WIDTH="2%"></TD>
<TD WIDTH="56%"></TD></TR>


<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><B>Issuer</B></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">Quanta Services, Inc.</P></TD></TR>
<TR STYLE="font-size:1pt">
<TD HEIGHT="8"></TD>
<TD HEIGHT="8" COLSPAN="2"></TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><B>Securities Offered</B></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="top"> <P STYLE="margin-top:0pt; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">$500,000,000 aggregate principal amount of 0.950% Senior Notes due 2024.</P>
<P STYLE="margin-top:0pt; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">$500,000,000 aggregate principal amount of 2.350% Senior Notes due 2032.</P>
<P STYLE="margin-top:0pt; margin-bottom:1pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">$500,000,000 aggregate principal amount of 3.050% Senior Notes due 2041.</P></TD></TR>
<TR STYLE="font-size:1pt">
<TD HEIGHT="8"></TD>
<TD HEIGHT="8" COLSPAN="2"></TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><B>Maturity Date</B></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="top"> <P STYLE="margin-top:0pt; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">2024 notes: October 1, 2024.</P>
<P STYLE="margin-top:0pt; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">2032 notes: January 15, 2032.</P>
<P STYLE="margin-top:0pt; margin-bottom:1pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">2041 notes: October 1, 2041.</P></TD></TR>
<TR STYLE="font-size:1pt">
<TD HEIGHT="8"></TD>
<TD HEIGHT="8" COLSPAN="2"></TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><B>Interest Rate</B></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="top">The 2024 notes will bear interest at a rate of 0.950% per annum, the 2032 notes will bear interest at a rate of 2.350% per annum, and the 2041 notes will bear interest at a rate of 3.050% per annum.</TD></TR>
<TR STYLE="font-size:1pt">
<TD HEIGHT="8"></TD>
<TD HEIGHT="8" COLSPAN="2"></TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><B>Interest Payment Dates</B></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="top"> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman">The 2024 notes will bear interest from, and including September&nbsp;23, 2021, payable semi-annually in arrears on April&nbsp;1 and
October&nbsp;1 of each year, commencing April&nbsp;1, 2022.</P> <P STYLE="font-size:12pt; margin-top:0pt; margin-bottom:0pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman">The 2032 notes will
bear interest from, and including September&nbsp;23, 2021, payable semi-annually in arrears on January&nbsp;15 and July&nbsp;15 of each year, commencing July&nbsp;15, 2022.</P> <P STYLE="font-size:12pt; margin-top:0pt; margin-bottom:0pt">&nbsp;</P>
<P STYLE="margin-top:0pt; margin-bottom:1pt; font-size:10pt; font-family:Times New Roman">The 2041 notes will bear interest from, and including September&nbsp;23, 2021, payable semi-annually in arrears on April&nbsp;1 and October&nbsp;1 of each
year, commencing April&nbsp;1, 2022.</P></TD></TR>
<TR STYLE="font-size:1pt">
<TD HEIGHT="8"></TD>
<TD HEIGHT="8" COLSPAN="2"></TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><B>Ranking</B></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="top"> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman">The notes will:</P> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<P STYLE="margin-top:0pt; margin-bottom:0pt; margin-left:2.00em; text-indent:-2.00em; font-size:10pt; font-family:Times New Roman">&#149;&#8195;&#8194;&#8202;be senior unsecured obligations of Quanta;</P>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; margin-left:2.00em; text-indent:-2.00em; font-size:10pt; font-family:Times New Roman">&#149;&#8195;&#8194;&#8202;rank equally in right
of payment with all existing and future senior unsecured indebtedness of Quanta, subject to applicable law;</P> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<P STYLE="margin-top:0pt; margin-bottom:0pt; margin-left:2.00em; text-indent:-2.00em; font-size:10pt; font-family:Times New Roman">&#149;&#8195;&#8194;&#8202;rank senior in right of payment to all future subordinated indebtedness of Quanta, if any,
subject to applicable law;</P> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<P STYLE="margin-top:0pt; margin-bottom:0pt; margin-left:2.00em; text-indent:-2.00em; font-size:10pt; font-family:Times New Roman">&#149;&#8195;&#8194;&#8202;be effectively subordinated to all secured indebtedness of Quanta, if any, to the extent of
the value of the assets securing such indebtedness; and</P> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<P STYLE="margin-top:0pt; margin-bottom:1pt; margin-left:2.00em; text-indent:-2.00em; font-size:10pt; font-family:Times New Roman">&#149;&#8195;&#8194;&#8202;be structurally subordinated to all liabilities, including trade payables, of the
subsidiaries of Quanta.</P></TD></TR></TABLE>
</div><br clear="All"></div>

 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">S-4 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">

<div style ="BORDER-BOTTOM:1.00pt solid #000000;BORDER-LEFT:1.00pt solid #000000;BORDER-RIGHT:1.00pt solid #000000;BORDER-TOP:1.00pt solid #000000;MARGIN-LEFT:0px; MARGIN-RIGHT:0px;max-width:100%"><div style="width:97%; margin-top:1.5%; margin-left:1.5%; margin-right:-1.25%">


<TABLE CELLSPACING="0" CELLPADDING="0" WIDTH="100%" BORDER="0" STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" ALIGN="center">


<TR>

<TD WIDTH="43%"></TD>

<TD VALIGN="bottom" WIDTH="2%"></TD>
<TD WIDTH="56%"></TD></TR>

<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="top"> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman">As of June&nbsp;30, 2021, as adjusted for this offering, the application of the net proceeds therefrom as set forth in &#147;Use of
Proceeds&#148; and an assumed amount of $750 million in borrowings under our new term loan facility (after giving effect to the credit agreement amendment, but prior to potentially financing the remainder of the cash portion of the consideration for
the Blattner Acquisition with borrowings under our revolving credit facility as set forth in &#147;Use of Proceeds&#148;), we would have had approximately $3.60 billion of outstanding debt, of which $53.7&nbsp;million would have been secured, and we
would have had $1.89&nbsp;billion of undrawn borrowing capacity under our revolving credit facility. The credit agreement amendment is being negotiated as of the date of this prospectus supplement and its effectiveness therefore remains subject to
market conditions and the satisfaction of certain conditions precedent, and there are no assurances that we will enter into the credit agreement amendment on the terms described herein, including the $750 million assumed size of our term loan
facility, or at all; if we enter into the credit agreement amendment, we will not be obligated to make any borrowings thereunder, but the commitments under the Bridge Facility would be permanently reduced by 100% of the commitments pursuant to our
term loan facility as long as the conditions to availability of our term loan facility are no more restrictive than the Bridge Facility.</P> <P STYLE="font-size:12pt; margin-top:0pt; margin-bottom:0pt">&nbsp;</P>
<P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman">As of June&nbsp;30, 2021, our subsidiaries had approximately $2.75&nbsp;billion of total liabilities (excluding intercompany liabilities) outstanding,
including trade payables.</P> <P STYLE="font-size:12pt; margin-top:0pt; margin-bottom:0pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:1pt; font-size:10pt; font-family:Times New Roman">For additional information, see &#147;Description of
Notes&#151;Ranking.&#148;</P></TD></TR>
<TR STYLE="font-size:1pt">
<TD HEIGHT="8"></TD>
<TD HEIGHT="8" COLSPAN="2"></TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><B>Optional Redemption</B></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE="margin-top:0pt; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><U>2024 notes</U></P> <P STYLE="font-size:6pt; margin-top:0pt; margin-bottom:0pt">&nbsp;</P>
<P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman">At our option, prior to October 1, 2022, we may redeem some or all of the 2024 notes, at any time and from time to time, at the applicable redemption price
described under &#147;Description of Notes&#151;Optional Redemption&#148; in this prospectus supplement. Commencing October 1, 2022, we may redeem some or all of the 2024 notes, at any time and from time to time, at a redemption price equal to 100%
of the principal amount of the 2024 notes being redeemed plus accrued and unpaid interest, if any, to (but excluding) the redemption date.</P> <P STYLE="font-size:12pt; margin-top:0pt; margin-bottom:0pt">&nbsp;</P>
<P STYLE="margin-top:0pt; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><U>2032 notes</U></P> <P STYLE="font-size:6pt; margin-top:0pt; margin-bottom:0pt">&nbsp;</P>
<P STYLE="margin-top:0pt; margin-bottom:1pt; font-size:10pt; font-family:Times New Roman">At our option, prior to October 15, 2031 (three months before the maturity date), we may redeem some or all of the 2032 notes, at any time and from time to
time, at the applicable redemption price described under &#147;Description of Notes&#151;Optional Redemption&#148; in this prospectus</P></TD></TR></TABLE>
</div><br clear="All"></div>

 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">S-5 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">

<div style ="BORDER-BOTTOM:1.00pt solid #000000;BORDER-LEFT:1.00pt solid #000000;BORDER-RIGHT:1.00pt solid #000000;BORDER-TOP:1.00pt solid #000000;MARGIN-LEFT:0px; MARGIN-RIGHT:0px;max-width:100%"><div style="width:97%; margin-top:1.5%; margin-left:1.5%; margin-right:-1.25%">


<TABLE CELLSPACING="0" CELLPADDING="0" WIDTH="100%" BORDER="0" STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" ALIGN="center">


<TR>

<TD WIDTH="43%"></TD>

<TD VALIGN="bottom" WIDTH="2%"></TD>
<TD WIDTH="56%"></TD></TR>

<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman">supplement. Commencing October 15, 2031, (three months before the maturity date), we may redeem some or all of the 2032 notes, at any time
and from time to time, at a redemption price equal to 100% of the principal amount of the 2032 notes being redeemed plus accrued and unpaid interest, if any, to (but excluding) the redemption date.</P>
<P STYLE="font-size:12pt; margin-top:0pt; margin-bottom:0pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><U>2041 notes</U></P>
<P STYLE="font-size:6pt; margin-top:0pt; margin-bottom:0pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:1pt; font-size:10pt; font-family:Times New Roman">At our option, prior to April 1, 2041, (six months before the maturity date), we may
redeem some or all of the 2041 notes, at any time and from time to time, at the applicable redemption price described under &#147;Description of Notes&#151;Optional Redemption&#148; in this prospectus supplement. Commencing April 1, 2041, (six
months before the maturity date), we may redeem some or all of the 2041 notes, at any time and from time to time, at a redemption price equal to 100% of the principal amount of the 2041 notes being redeemed plus accrued and unpaid interest, if any,
to (but excluding) the redemption date.</P></TD></TR>
<TR STYLE="font-size:1pt">
<TD HEIGHT="16"></TD>
<TD HEIGHT="16" COLSPAN="2"></TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><B>Special Mandatory Redemption</B></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="bottom">In the event that (x) the Blattner Acquisition is not consummated on or prior to June 30, 2022 or (y) the Merger Agreement is terminated without the Blattner Acquisition being consummated, we will be required to redeem all of the
outstanding 2024 notes, 2032 notes and 2041 notes at a redemption price equal to 101% of the aggregate principal amount of the 2024 notes, 2032 notes and 2041 notes, respectively, plus accrued and unpaid interest, if any, to (but excluding) the
redemption date. See &#147;Description of Notes&#151;Special&nbsp;Mandatory&nbsp;Redemption.&#148;</TD></TR>
<TR STYLE="font-size:1pt">
<TD HEIGHT="8"></TD>
<TD HEIGHT="8" COLSPAN="2"></TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><B>Covenants</B></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman">The indenture governing the notes contains covenants limiting our ability and/or certain of our subsidiaries&#146; ability to:</P>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; margin-left:2.00em; text-indent:-2.00em; font-size:10pt; font-family:Times New Roman">&#149;&#8195;&#8194;&#8202;create certain
liens;</P> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; margin-left:2.00em; text-indent:-2.00em; font-size:10pt; font-family:Times New Roman">&#149;&#8195;&#8194;&#8202;enter into
sale and leaseback transactions; and</P> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<P STYLE="margin-top:0pt; margin-bottom:0pt; margin-left:2.00em; text-indent:-2.00em; font-size:10pt; font-family:Times New Roman">&#149;&#8195;&#8194;&#8202;consolidate or merge with, or convey, transfer or lease all or substantially all our assets
to, another person.</P> <P STYLE="font-size:12pt; margin-top:0pt; margin-bottom:0pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:1pt; font-size:10pt; font-family:Times New Roman">However, each of these covenants is subject to a number of
significant exceptions. You should read &#147;Description of Notes&#151;Certain Covenants&#148; for more information regarding these covenants.</P></TD></TR>
<TR STYLE="font-size:1pt">
<TD HEIGHT="8"></TD>
<TD HEIGHT="8" COLSPAN="2"></TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><B>Change of Control Triggering Event</B></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE="margin-top:0pt; margin-bottom:1pt; font-size:10pt; font-family:Times New Roman">If a Change of Control Triggering Event (as defined in &#147;Description of Notes&#151;Purchase upon a Change of Control Triggering
Event&#148;) occurs, except to the extent we have</P></TD></TR>
<TR STYLE="font-size:1pt">
<TD HEIGHT="8"></TD>
<TD HEIGHT="8" COLSPAN="2"></TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="bottom"></TD></TR></TABLE>
</div><br clear="All"></div>

 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">S-6 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">

<div style ="BORDER-BOTTOM:1.00pt solid #000000;BORDER-LEFT:1.00pt solid #000000;BORDER-RIGHT:1.00pt solid #000000;BORDER-TOP:1.00pt solid #000000;MARGIN-LEFT:0px; MARGIN-RIGHT:0px;max-width:100%"><div style="width:97%; margin-top:1.5%; margin-left:1.5%; margin-right:-1.25%">


<TABLE CELLSPACING="0" CELLPADDING="0" WIDTH="100%" BORDER="0" STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" ALIGN="center">


<TR>

<TD WIDTH="43%"></TD>

<TD VALIGN="bottom" WIDTH="2%"></TD>
<TD WIDTH="56%"></TD></TR>

<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="bottom">exercised our right to redeem the notes, you will have the right to require us to purchase all or any part of your notes at a purchase price equal to 101% of the principal amount, plus accrued and unpaid interest, if any, on such
notes, to, but excluding, the purchase date. See &#147;Description of Notes&#151;Purchase upon a Change of Control Triggering Event.&#148;</TD></TR>
<TR STYLE="font-size:1pt">
<TD HEIGHT="8"></TD>
<TD HEIGHT="8" COLSPAN="2"></TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><B>Form and Denomination of Notes</B></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="top">The notes will be issued in fully registered form only and will initially be represented by one or more global notes which will be deposited with a custodian for, and registered in the name of a nominee of, The Depository Trust
Company (the &#147;Depositary&#148;). The notes will be issued only in registered form in minimum denominations of $2,000 and integral multiples of $1,000 in excess thereof in book-entry form only. See &#147;Description of Notes&#151;Book-entry
System.&#148;</TD></TR>
<TR STYLE="font-size:1pt">
<TD HEIGHT="8"></TD>
<TD HEIGHT="8" COLSPAN="2"></TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><B>Absence of Established Market for Notes</B></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="top">The notes will be new issues of securities for which there is no established market. Accordingly, there can be no assurance that a market for the notes will develop or as to the liquidity of any market that may develop. The
underwriters have advised us that they currently intend to make a market in the notes. However, they are not obligated to do so, and any market-making with respect to the notes may be discontinued without notice. We do not intend to list the notes
on any securities exchange or public market or include the notes in any quotation system.</TD></TR>
<TR STYLE="font-size:1pt">
<TD HEIGHT="8"></TD>
<TD HEIGHT="8" COLSPAN="2"></TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><B>Use of Proceeds</B></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="top"> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman">We intend to use the net proceeds from this offering, together with borrowings under our term loan facility, as well as borrowings under our
revolving credit facility or cash on hand, or a combination thereof, if necessary, to finance the cash portion of the consideration for the Blattner Acquisition.</P> <P STYLE="font-size:12pt; margin-top:0pt; margin-bottom:0pt">&nbsp;</P>
<P STYLE="margin-top:0pt; margin-bottom:1pt; font-size:10pt; font-family:Times New Roman">If the Blattner Acquisition is not consummated prior to a Special Mandatory Redemption Event, we intend to use the net proceeds from the notes, together with
borrowings under our revolving credit facility or cash on hand, or a combination thereof, if necessary, to fund the special mandatory redemption of the notes described in &#147;Description of Notes&#151;Special Mandatory Redemption.&#148; See
&#147;Use of Proceeds.&#148;</P></TD></TR>
<TR STYLE="font-size:1pt">
<TD HEIGHT="8"></TD>
<TD HEIGHT="8" COLSPAN="2"></TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><B>Conflicts of Interest</B></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="top">Affiliates of BofA Securities, Inc. and Wells Fargo Securities LLC have provided commitments under the Bridge Facility. In the event that the Bridge Facility is funded prior to completion of this offering, we will be required to use
the net proceeds of this offering to prepay the amounts outstanding under the Bridge Facility on a <FONT STYLE="white-space:nowrap"><FONT STYLE="white-space:nowrap">dollar-for-dollar</FONT></FONT> basis. As such, at least 5% or more of the net
proceeds of this offering (not including underwriting discounts) may be directed to one or more of the underwriters or their affiliates. The receipt of at least 5% of the net proceeds of this offering by any underwriter (or its affiliates) would be
considered a &#147;conflict of interest&#148; under</TD></TR></TABLE>
</div><br clear="All"></div>

 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">S-7 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">

<div style ="BORDER-BOTTOM:1.00pt solid #000000;BORDER-LEFT:1.00pt solid #000000;BORDER-RIGHT:1.00pt solid #000000;BORDER-TOP:1.00pt solid #000000;MARGIN-LEFT:0px; MARGIN-RIGHT:0px;max-width:100%"><div style="width:97%; margin-top:1.5%; margin-left:1.5%; margin-right:-1.25%">


<TABLE CELLSPACING="0" CELLPADDING="0" WIDTH="100%" BORDER="0" STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" ALIGN="center">


<TR>

<TD WIDTH="43%"></TD>

<TD VALIGN="bottom" WIDTH="2%"></TD>
<TD WIDTH="56%"></TD></TR>

<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="top"> <P STYLE="margin-top:0pt; margin-bottom:1pt; font-size:10pt; font-family:Times New Roman">FINRA Rule 5121 regarding the underwriting of securities of a company with a member that has a conflict of interest within the meaning of
those rules. Pursuant to that rule, the appointment of a &#147;qualified independent underwriter&#148; (as such term is defined in FINRA Rule 5121) is not necessary in connection with this offering as the securities offered are investment grade
rated, as that term is defined in the rule. In accordance with FINRA Rule 5121, the underwriters with a conflict of interest will not confirm sales of notes to any account over which they exercise discretionary authority without prior written
approval of the customer. See &#147;Underwriting (Conflicts of Interest).&#148;</P></TD></TR>
<TR STYLE="font-size:1pt">
<TD HEIGHT="8"></TD>
<TD HEIGHT="8" COLSPAN="2"></TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><B>Trustee</B></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">U.S. Bank National Association.</P></TD></TR>
<TR STYLE="font-size:1pt">
<TD HEIGHT="8"></TD>
<TD HEIGHT="8" COLSPAN="2"></TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><B>Governing Law</B></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">New York.</P></TD></TR>
<TR STYLE="font-size:1pt">
<TD HEIGHT="8"></TD>
<TD HEIGHT="8" COLSPAN="2"></TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><B>Risk Factors</B></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="top">Investing in the notes involves certain risks. See &#147;<A HREF="#supprom326517_5">Risk Factors</A>&#148; beginning on page <FONT STYLE="white-space:nowrap">S-11</FONT> of this prospectus supplement and on page 2 of the
accompanying prospectus for a description of certain risks you should consider before investing in the notes.</TD></TR>
</TABLE>
</div><br clear="All"></div>

 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">S-8 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">

<div style ="BORDER-BOTTOM:1.00pt solid #000000;BORDER-LEFT:1.00pt solid #000000;BORDER-RIGHT:1.00pt solid #000000;BORDER-TOP:1.00pt solid #000000;MARGIN-LEFT:0px; MARGIN-RIGHT:0px;max-width:100%"><div style="width:97%; margin-top:1.5%; margin-left:1.5%; margin-right:-1.25%">

 <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center"><B>Summary Historical Consolidated Financial Data of Quanta </B></P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The summary historical consolidated financial data as of December&nbsp;31, 2020 and 2019 and for each of the three years in the period ended
December&nbsp;31, 2020 set forth below are derived from our audited consolidated financial statements and are qualified in their entirety by, and should be read in conjunction with, our audited consolidated financial statements and notes related
thereto in our 2020 Annual Report and &#147;Management&#146;s Discussion and Analysis of Financial Condition and Results of Operations&#148; included in our 2020 Annual Report. The summary historical consolidated financial data as of
December&nbsp;31, 2018 set forth below was derived from our audited consolidated financial statements and notes thereto not incorporated by reference in this prospectus supplement. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The summary historical condensed consolidated financial data as of June&nbsp;30, 2021 and for the six months ended June&nbsp;30, 2021 and 2020
set forth below are derived from our unaudited condensed consolidated financial statements and are qualified in their entirety by, and should be read in conjunction with, our unaudited condensed consolidated financial statements and notes related
thereto in our Q2 Quarterly Report and &#147;Management&#146;s Discussion and Analysis of Financial Condition and Results of Operations&#148; included in our Q2 Quarterly Report. The preparation of the unaudited condensed consolidated financial
statements in conformity with accounting principles generally accepted in the United States of America (&#147;GAAP&#148;) requires the use of estimates and assumptions by management in determining the reported amounts of assets and liabilities,
disclosures of contingent assets and liabilities known to exist as of the date the financial statements are published, and the reported amounts of revenues and expenses recognized during the periods presented. We review all significant estimates
affecting our consolidated financial statements on a recurring basis and record the effect of any necessary adjustments prior to their publication. Judgments and estimates are based on our belief and assumption derived from information available at
the time such judgments and estimates are made. Actual results could differ from those estimates. The interim financial data as of June&nbsp;30, 2021 and for the six months ended June&nbsp;30, 2021 and June&nbsp;30, 2020 is unaudited. In the opinion
of management, the interim financial data includes all adjustments, consisting only of normal recurring adjustments, necessary to a fair statement of the results for the interim periods. The results of operations for the six months ended
June&nbsp;30, 2021 are not necessarily indicative of the results that may be expected for the year ending December&nbsp;31, 2021. </P> <P STYLE="font-size:12pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE CELLSPACING="0" CELLPADDING="0" WIDTH="100%" BORDER="0" STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" ALIGN="center">


<TR>

<TD WIDTH="47%"></TD>

<TD VALIGN="bottom" WIDTH="1%"></TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TD VALIGN="bottom" WIDTH="1%"></TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TD VALIGN="bottom" WIDTH="1%"></TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TD VALIGN="bottom" WIDTH="1%"></TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TD VALIGN="bottom" WIDTH="1%"></TD>
<TD></TD>
<TD></TD>
<TD></TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:8pt">
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom" COLSPAN="6" ALIGN="center" STYLE="border-bottom:1.00pt solid #000000"><B>Six Months Ended</B><br><B>June&nbsp;30,</B></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom" COLSPAN="10" ALIGN="center" STYLE="border-bottom:1.00pt solid #000000"><B>Year Ended</B><br><B>December&nbsp;31,</B></TD>
<TD VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:8pt">
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom" COLSPAN="2" ALIGN="center" STYLE="border-bottom:1.00pt solid #000000"><B>2021</B></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom" COLSPAN="2" ALIGN="center" STYLE="border-bottom:1.00pt solid #000000"><B>2020</B></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom" COLSPAN="2" ALIGN="center" STYLE="border-bottom:1.00pt solid #000000"><B>2020</B></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom" COLSPAN="2" ALIGN="center" STYLE="border-bottom:1.00pt solid #000000"><B>2019</B></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom" COLSPAN="2" ALIGN="center" STYLE="border-bottom:1.00pt solid #000000"><B>2018</B></TD>
<TD VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:8pt">
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom" COLSPAN="18" ALIGN="center">(in thousands, except per share information)</TD>
<TD VALIGN="bottom">&nbsp;</TD></TR>


<TR BGCOLOR="#cceeff" STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">Consolidated Statements of Operations Data:</P></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom"></TD>
<TD VALIGN="bottom"></TD>
<TD VALIGN="bottom"></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom"></TD>
<TD VALIGN="bottom"></TD>
<TD VALIGN="bottom"></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom"></TD>
<TD VALIGN="bottom"></TD>
<TD VALIGN="bottom"></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom"></TD>
<TD VALIGN="bottom"></TD>
<TD VALIGN="bottom"></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom"></TD>
<TD VALIGN="bottom"></TD>
<TD VALIGN="bottom"></TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">Revenues</P></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">5,703,397</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">5,270,326</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">11,202,672</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">12,112,153</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">11,171,423</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR BGCOLOR="#cceeff" STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">Cost of services (including depreciation)</P></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">4,882,796</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">4,582,866</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">9,541,825</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">10,511,901</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">9,691,459</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="font-size:1px; ">
<TD VALIGN="bottom"></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD>&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD>&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD>&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD>&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD>&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:3.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">Gross profit</P></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">820,601</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">687,460</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">1,660,847</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">1,600,252</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">1,479,964</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR BGCOLOR="#cceeff" STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">Equity in earnings of integral unconsolidated affiliates</P></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">12,633</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">1,045</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">11,303</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">&#151;&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">&#151;&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">Selling, general and administrative expenses</P></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">(513,462</TD>
<TD NOWRAP VALIGN="bottom">)&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">(458,645</TD>
<TD NOWRAP VALIGN="bottom">)&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">(975,074</TD>
<TD NOWRAP VALIGN="bottom">)&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">(955,991</TD>
<TD NOWRAP VALIGN="bottom">)&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">(857,574</TD>
<TD NOWRAP VALIGN="bottom">)&nbsp;</TD></TR>
<TR BGCOLOR="#cceeff" STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">Amortization of intangible assets</P></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">(42,646</TD>
<TD NOWRAP VALIGN="bottom">)&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">(35,687</TD>
<TD NOWRAP VALIGN="bottom">)&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">(76,704</TD>
<TD NOWRAP VALIGN="bottom">)&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">(62,091</TD>
<TD NOWRAP VALIGN="bottom">)&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">(43,994</TD>
<TD NOWRAP VALIGN="bottom">)&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">Asset impairment charges (a)</P></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">(2,319</TD>
<TD NOWRAP VALIGN="bottom">)&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">&#151;&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">(8,282</TD>
<TD NOWRAP VALIGN="bottom">)&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">(13,892</TD>
<TD NOWRAP VALIGN="bottom">)&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">(49,375</TD>
<TD NOWRAP VALIGN="bottom">)&nbsp;</TD></TR>
<TR BGCOLOR="#cceeff" STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">Change in fair value of contingent consideration liabilities</P></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">573</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">(520</TD>
<TD NOWRAP VALIGN="bottom">)&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">(719</TD>
<TD NOWRAP VALIGN="bottom">)&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">(13,404</TD>
<TD NOWRAP VALIGN="bottom">)&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">11,248</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="font-size:1px; ">
<TD VALIGN="bottom"></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD>&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD>&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD>&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD>&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD>&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:3.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">Operating income</P></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">275,380</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">193,653</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">611,371</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">554,874</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">540,269</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR BGCOLOR="#cceeff" STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">Interest expense</P></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">(25,584</TD>
<TD NOWRAP VALIGN="bottom">)&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">(22,660</TD>
<TD NOWRAP VALIGN="bottom">)&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">(45,013</TD>
<TD NOWRAP VALIGN="bottom">)&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">(66,890</TD>
<TD NOWRAP VALIGN="bottom">)&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">(36,945</TD>
<TD NOWRAP VALIGN="bottom">)&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">Interest income</P></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">3,026</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">1,034</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">2,449</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">927</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">1,555</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR BGCOLOR="#cceeff" STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">Other income (expense), net (b)</P></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">12,143</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">(6,580</TD>
<TD NOWRAP VALIGN="bottom">)&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">2,539</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">83,376</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">(47,213</TD>
<TD NOWRAP VALIGN="bottom">)&nbsp;</TD></TR>
<TR STYLE="font-size:1px; ">
<TD VALIGN="bottom"></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD>&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD>&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD>&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD>&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD>&nbsp;</TD></TR></TABLE>
</div><br clear="All"></div>

 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">S-9 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">

<div style ="BORDER-BOTTOM:1.00pt solid #000000;BORDER-LEFT:1.00pt solid #000000;BORDER-RIGHT:1.00pt solid #000000;BORDER-TOP:1.00pt solid #000000;MARGIN-LEFT:0px; MARGIN-RIGHT:0px;max-width:100%"><div style="width:97%; margin-top:1.5%; margin-left:1.5%; margin-right:-1.25%">


<TABLE CELLSPACING="0" CELLPADDING="0" WIDTH="100%" BORDER="0" STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" ALIGN="center">


<TR>

<TD WIDTH="50%"></TD>

<TD VALIGN="bottom" WIDTH="3%"></TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TD VALIGN="bottom" WIDTH="3%"></TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TD VALIGN="bottom" WIDTH="3%"></TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TD VALIGN="bottom" WIDTH="3%"></TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TD VALIGN="bottom" WIDTH="3%"></TD>
<TD></TD>
<TD></TD>
<TD></TD></TR>

<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:8pt">
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom" COLSPAN="6" ALIGN="center" STYLE="border-bottom:1.00pt solid #000000"><B>Six Months Ended</B><br><B>June&nbsp;30,</B></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom" COLSPAN="10" ALIGN="center" STYLE="border-bottom:1.00pt solid #000000"><B>Year Ended</B><br><B>December&nbsp;31,</B></TD>
<TD VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:8pt">
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom" COLSPAN="2" ALIGN="center" STYLE="border-bottom:1.00pt solid #000000"><B>2021</B></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom" COLSPAN="2" ALIGN="center" STYLE="border-bottom:1.00pt solid #000000"><B>2020</B></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom" COLSPAN="2" ALIGN="center" STYLE="border-bottom:1.00pt solid #000000"><B>2020</B></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom" COLSPAN="2" ALIGN="center" STYLE="border-bottom:1.00pt solid #000000"><B>2019</B></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom" COLSPAN="2" ALIGN="center" STYLE="border-bottom:1.00pt solid #000000"><B>2018</B></TD>
<TD VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:8pt">
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom" COLSPAN="18" ALIGN="center">(in thousands, except per share information)</TD>
<TD VALIGN="bottom">&nbsp;</TD></TR>


<TR BGCOLOR="#cceeff" STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">Income before income taxes</P></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">264,965</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">165,447</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">571,346</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">572,287</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">457,666</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">Provision for income taxes (c)</P></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">54,675</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">49,149</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">119,387</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">165,472</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">161,659</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="font-size:1px; ">
<TD VALIGN="bottom"></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD>&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD>&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD>&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD>&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD>&nbsp;</TD></TR>
<TR BGCOLOR="#cceeff" STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:3.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">Net income</P></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">210,290</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">116,298</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">451,959</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">406,815</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">296,007</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">Less: Net income attributable to <FONT STYLE="white-space:nowrap">non-controlling</FONT>
interests</P></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">3,496</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">3,666</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">6,363</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">4,771</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">2,661</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="font-size:1px; ">
<TD VALIGN="bottom"></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD>&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD>&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD>&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD>&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD>&nbsp;</TD></TR>
<TR BGCOLOR="#cceeff" STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:3.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">Net income attributable to common stock</P></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">206,794</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">112,632</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">445,596</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">402,044</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">293,346</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="font-size:1px; ">
<TD VALIGN="bottom"></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:3.00px double #000000">&nbsp;</P></TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:3.00px double #000000">&nbsp;</P></TD>
<TD>&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:3.00px double #000000">&nbsp;</P></TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:3.00px double #000000">&nbsp;</P></TD>
<TD>&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:3.00px double #000000">&nbsp;</P></TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:3.00px double #000000">&nbsp;</P></TD>
<TD>&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:3.00px double #000000">&nbsp;</P></TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:3.00px double #000000">&nbsp;</P></TD>
<TD>&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:3.00px double #000000">&nbsp;</P></TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:3.00px double #000000">&nbsp;</P></TD>
<TD>&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">Earnings per share attributable to common stock:</P></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom"></TD>
<TD VALIGN="bottom"></TD>
<TD VALIGN="bottom"></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom"></TD>
<TD VALIGN="bottom"></TD>
<TD VALIGN="bottom"></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom"></TD>
<TD VALIGN="bottom"></TD>
<TD VALIGN="bottom"></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom"></TD>
<TD VALIGN="bottom"></TD>
<TD VALIGN="bottom"></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom"></TD>
<TD VALIGN="bottom"></TD>
<TD VALIGN="bottom"></TD></TR>
<TR BGCOLOR="#cceeff" STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:3.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">Basic</P></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">1.48</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">0.79</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">3.15</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">2.76</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">1.92</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="font-size:1px; ">
<TD VALIGN="bottom"></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:3.00px double #000000">&nbsp;</P></TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:3.00px double #000000">&nbsp;</P></TD>
<TD>&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:3.00px double #000000">&nbsp;</P></TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:3.00px double #000000">&nbsp;</P></TD>
<TD>&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:3.00px double #000000">&nbsp;</P></TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:3.00px double #000000">&nbsp;</P></TD>
<TD>&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:3.00px double #000000">&nbsp;</P></TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:3.00px double #000000">&nbsp;</P></TD>
<TD>&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:3.00px double #000000">&nbsp;</P></TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:3.00px double #000000">&nbsp;</P></TD>
<TD>&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:3.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">Diluted</P></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">1.43</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">0.78</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">3.07</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">2.73</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">1.90</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="font-size:1px; ">
<TD VALIGN="bottom"></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:3.00px double #000000">&nbsp;</P></TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:3.00px double #000000">&nbsp;</P></TD>
<TD>&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:3.00px double #000000">&nbsp;</P></TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:3.00px double #000000">&nbsp;</P></TD>
<TD>&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:3.00px double #000000">&nbsp;</P></TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:3.00px double #000000">&nbsp;</P></TD>
<TD>&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:3.00px double #000000">&nbsp;</P></TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:3.00px double #000000">&nbsp;</P></TD>
<TD>&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:3.00px double #000000">&nbsp;</P></TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:3.00px double #000000">&nbsp;</P></TD>
<TD>&nbsp;</TD></TR>
</TABLE> <P STYLE="line-height:8.0pt;margin-top:0pt;margin-bottom:2pt;border-bottom:1px solid #000000;width:11%">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%" VALIGN="top" ALIGN="left">(a)</TD>
<TD ALIGN="left" VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman; " ALIGN="left">In the six months ended June&nbsp;30, 2021, we recorded an asset impairment charge of $2.3&nbsp;million
($1.7&nbsp;million net of tax) related to the planned sale of certain equipment that is not utilized in Quanta&#146;s core operations. In the years ended December&nbsp;31, 2020, 2019 and 2018, we recorded asset impairment charges of
$8.3&nbsp;million ($7.9&nbsp;million net of tax), $13.9&nbsp;million ($10.5&nbsp;million net of tax) and $49.4&nbsp;million ($36.5&nbsp;million net of tax). The charges recorded in 2020 related to the exit of our Latin American operations and the
planned sale of certain equipment that is not utilized in Quanta&#146;s core operations. The charges recorded in 2019 related to the winding down and exit of certain <FONT STYLE="white-space:nowrap">oil-influenced</FONT> operations and assets, the
replacement of an internally-developed software application and the planned sale of certain foreign operations and assets. The charges recorded in 2018 primarily related to the winding down of certain
<FONT STYLE="white-space:nowrap">oil-influenced</FONT> operations and assets. </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%" VALIGN="top" ALIGN="left">(b)</TD>
<TD ALIGN="left" VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman; " ALIGN="left">In the year ended December&nbsp;31, 2019, we recognized $60.3&nbsp;million of earnings that were previously
deferred in prior periods related to our equity investment in a large electric transmission project in Canada that was substantially completed and placed into commercial operation during the three months ended March&nbsp;31, 2019. The majority of
these deferred profits were attributable to profit earned and deferred in the years ended December&nbsp;31, 2018 and 2017. We also recognized a gain of $13.0&nbsp;million from the sale of this equity investment during the three months ended
December&nbsp;31, 2019. </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%" VALIGN="top" ALIGN="left">(c)</TD>
<TD ALIGN="left" VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman; " ALIGN="left">The effective tax rate in the year ended December&nbsp;31, 2019 was impacted by a $79.2&nbsp;million charge in
the period associated with a terminated telecommunications project in Peru, for which no income tax benefit was recognized. For information on additional items that impacted the effective tax rates in 2021, 2020 and 2019, refer to &#147;Results of
Operations&#151;Consolidated Results&#151;Provision for income taxes&#148; included in &#147;Management&#146;s Discussion and Analysis of Financial Condition and Results of Operations&#148; included in the Q2 Quarterly Report and the 2020 Annual
Report. The effective tax rate in the year ended December&nbsp;31, 2018 was primarily impacted by a $37.2&nbsp;million provision to record a valuation allowance against certain tax benefits recognized during 2017 associated with the Tax Cuts and
Jobs Act of 2017 and other entity restructuring and recapitalization efforts. </P></TD></TR></TABLE> <P STYLE="font-size:12pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE CELLSPACING="0" CELLPADDING="0" WIDTH="92%" BORDER="0" STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" ALIGN="center">


<TR>

<TD WIDTH="52%"></TD>

<TD VALIGN="bottom" WIDTH="3%"></TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TD VALIGN="bottom" WIDTH="3%"></TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TD VALIGN="bottom" WIDTH="3%"></TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TD VALIGN="bottom" WIDTH="3%"></TD>
<TD></TD>
<TD></TD>
<TD></TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:8pt">
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom" COLSPAN="2" ALIGN="center" STYLE="border-bottom:1.00pt solid #000000"><B>June&nbsp;30,</B></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="bottom" COLSPAN="10" ALIGN="center" STYLE="border-bottom:1.00pt solid #000000"><B>December&nbsp;31,</B></TD>
<TD VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:8pt">
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom" COLSPAN="2" ALIGN="center" STYLE="border-bottom:1.00pt solid #000000"><B>2021</B></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="bottom" COLSPAN="2" ALIGN="center" STYLE="border-bottom:1.00pt solid #000000"><B>2020</B></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="bottom" COLSPAN="2" ALIGN="center" STYLE="border-bottom:1.00pt solid #000000"><B>2019</B></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="bottom" COLSPAN="2" ALIGN="center" STYLE="border-bottom:1.00pt solid #000000"><B>2018</B></TD>
<TD VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:8pt">
<TD VALIGN="bottom"><B>Balance Sheet Data:</B></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom" COLSPAN="14" ALIGN="center"><B>(in thousands)</B></TD>
<TD VALIGN="bottom">&nbsp;</TD></TR>


<TR BGCOLOR="#cceeff" STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">Working capital</P></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">1,602,802</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">1,449,833</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">1,567,937</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">1,519,977</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">Goodwill</P></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">2,136,133</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">2,121,014</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">2,022,675</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">1,899,879</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR BGCOLOR="#cceeff" STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">Total assets</P></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">8,720,596</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">8,398,272</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">8,331,682</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">7,075,787</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">Long-term debt, net of current maturities</P></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">1,353,542</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">1,174,294</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">1,292,195</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">1,040,532</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR BGCOLOR="#cceeff" STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">Total stockholders&#146; equity</P></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">4,486,732</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">4,344,181</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">4,050,292</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">3,604,159</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
</TABLE>
</div><br clear="All"></div>

 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">S-10 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center"><B><A NAME="supprom326517_5"></A>RISK FACTORS </B></P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman"><I>You should carefully consider each of the following risks, the risks discussed under the heading &#147;Risk Factors&#148; in the
accompanying prospectus and all of the information set forth or incorporated by reference in this prospectus supplement and the accompanying prospectus, including the risks described in our 2020 Annual Report in Item 1A. &#147;Risk Factors,&#148; in
our Q2 Quarterly Report in Item 1A. &#147;Risk Factors&#148; and any other documents we file with the SEC that are incorporated by reference in this prospectus supplement and the accompanying prospectus, before investing in the notes. </I></P>
<P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B>Risks Relating to the Notes </B></P> <P STYLE="margin-top:6pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B><I>We have a significant
amount of debt, which may increase as a result of this offering. Our substantial indebtedness could adversely affect our business, financial condition and results of operations and our ability to meet our payment obligations under the notes and our
other debt. </I></B></P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">We have a significant amount of debt and substantial debt service requirements. As of June&nbsp;30, 2021, as adjusted
for this offering, the application of the net proceeds therefrom to finance the cash portion of the consideration for the Blattner Acquisition as set forth in &#147;Use of Proceeds&#148; and an assumed amount of $750 million in borrowings under our
new term loan facility (after giving effect to the credit agreement amendment, but prior to potentially financing the remainder of the cash portion of the consideration for the Blattner Acquisition with borrowings under our revolving credit facility
as set forth in &#147;Use of Proceeds&#148;), we would have had approximately $3.60 billion of outstanding debt, of which $53.7&nbsp;million would have been secured, and we would have had $1.89&nbsp;billion of undrawn borrowing capacity under our
revolving credit facility. The credit agreement amendment is being negotiated as of the date of this prospectus supplement and its effectiveness therefore remains subject to market conditions and the satisfaction of certain conditions precedent, and
there are no assurances that we will enter into the credit agreement amendment on the terms described herein, including the $750 million assumed size of our term loan facility, or at all; if we enter into the credit agreement amendment, we will not
be obligated to make any borrowings thereunder, but the commitments under the Bridge Facility would be permanently reduced by 100% of the commitments pursuant to our term loan facility as long as the conditions to availability of our term loan
facility are no more restrictive than the Bridge Facility. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">This level of debt could have significant consequences on our future
operations, including: </P> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="4%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">making it more difficult for us to meet our payment and other obligations under the notes and our other
outstanding debt; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="4%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">resulting in an event of default if we fail to comply with the financial and other restrictive covenants
contained in our debt agreements, which event of default could result in all of our debt becoming immediately due and payable; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="4%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">reducing the availability of our cash flows to fund working capital, capital expenditures, acquisitions or
strategic investments, dividends and other general corporate purposes, and limiting our ability to obtain additional financing for these purposes; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="4%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">subjecting us to the risk of increasing interest expense on variable rate indebtedness, including borrowings
under our existing credit facility; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="4%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">limiting our flexibility in planning for, or reacting to, and increasing our vulnerability to, changes in our
business, the industry in which we operate and the general economy; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="4%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">limiting our ability to pursue business opportunities that become available to us; and </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="4%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">placing us at a competitive disadvantage compared to our competitors that have less debt or are less leveraged.
</P></TD></TR></TABLE> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Any of the above-listed factors could have an adverse effect on our business, financial condition and results of
operations and our ability to meet our payment obligations under the notes and our other debt. </P>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">S-11 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B><I>Servicing our debt requires a significant amount of cash, and we may not have sufficient cash flow
from our operations to pay our indebtedness. </I></B></P> <P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Our ability to generate cash in order to make scheduled payments of the principal of,
to pay interest on or to refinance our indebtedness, including the notes, depends on our future performance, which is subject to economic, financial, competitive, legislative, regulatory and other factors beyond our control. In addition, our ability
to borrow funds in the future to make payments on our debt will depend on the satisfaction of the covenants in our existing credit facility and our other financing agreements, including the indenture governing the notes, and other agreements we may
enter into in the future. Specifically, we will need to maintain certain financial ratios. Our business may not continue to generate sufficient cash flow from operations in the future and future borrowings may not be available to us under our
existing credit facility or from other sources in an amount sufficient to service our indebtedness, including the notes, to make necessary capital expenditures or to fund our other liquidity needs. If we are unable to generate cash from our
operations or through borrowings, we may be required to adopt one or more alternatives, such as selling assets, restructuring debt or obtaining additional equity capital on terms that may be onerous or highly dilutive. Our ability to make payments
on our indebtedness or refinance our indebtedness will depend on factors including the state of the capital markets and our financial condition at such time, as well as the terms of our financing agreements and the indenture governing the notes. We
may not be able to engage in any of these activities or engage in these activities on desirable terms, which could result in a default on our debt obligations. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B><I>We may incur substantial additional indebtedness, including debt ranking effectively senior to the notes, which could further exacerbate the risks
associated with our substantial indebtedness. </I></B></P> <P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Subject to the restrictions in our existing credit facility, we and our subsidiaries
may be able to incur additional indebtedness, including debt ranking effectively senior to the notes, in the future. In addition, the indenture governing the notes will not contain restrictions on the incurrence of additional debt, except for
certain debt secured by liens. Although our existing credit facility does contain restrictions on the incurrence of additional debt, these restrictions are subject to a number of significant qualifications and exceptions, including the ability of
Quanta Services, Inc. and our foreign subsidiaries to incur any amount of additional unsecured indebtedness as long as we comply with the existing credit facility&#146;s financial covenants, and the ability, on a
<FONT STYLE="white-space:nowrap">non-committed</FONT> basis, for us to increase revolving commitments and term loans under our existing credit facility up to the Incremental Cap (as defined in our existing credit facility), and debt incurred in
compliance with these restrictions could be substantial. If new debt is added to our and our subsidiaries&#146; existing debt levels, the related risks we now face would increase. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B><I>The notes will be effectively subordinated to all existing and future secured indebtedness of us and our subsidiaries. </I></B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The notes will not be secured by any of our assets or those of our subsidiaries. As a result, the notes will be effectively subordinated to our
existing secured debt and any secured debt we or our subsidiaries may incur to the extent of the value of the assets securing such debt. As of June&nbsp;30, 2021, on an as adjusted basis for this offering, the application of the net proceeds
therefrom to finance the cash portion of the consideration for the Blattner Acquisition as set forth in &#147;Use of Proceeds&#148; and an assumed amount of $750 million in borrowings under our new term loan facility (after giving effect to the
credit agreement amendment, but prior to potentially financing the remainder of the cash portion of the consideration for the Blattner Acquisition with borrowings under our revolving credit facility as set forth in &#147;Use of Proceeds&#148;), we
would have had approximately $3.60 billion of consolidated indebtedness outstanding, of which $53.7&nbsp;million would have been secured. In addition, after giving effect to the expected term loan facility in an amount we expect to be $750 million,
the aggregate amount of credit facilities under our credit agreement would increase from $2.51&nbsp;billion to $3.26 billion. In any liquidation, dissolution, bankruptcy or other similar proceeding, holders of our secured debt may assert rights
against any assets securing such debt in order to receive full payment of their debt before those assets may be used to pay the holders of the notes. To the extent that such assets cannot satisfy in full our secured debt, the holders of such secured
debt would have a claim for any shortfall that would rank equally in right of payment with the notes. In such an event, we may not have sufficient assets remaining to pay amounts due on any or all of the notes. If new indebtedness is added to our
current debt levels, the related risks we could face would be magnified. </P>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">S-12 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B><I>The notes will be structurally subordinated to all existing and future obligations of our
subsidiaries. </I></B></P> <P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Our equity interests in our subsidiaries are subordinate to any debt and other liabilities of our subsidiaries
(including trade payables, but excluding intercompany obligations and liabilities of a type not required to be reflected on a balance sheet of such subsidiaries in accordance with GAAP) to the extent of the value of the assets of such subsidiaries,
whether or not secured. The notes will not be guaranteed by our subsidiaries and we may not have direct access to the assets of our subsidiaries unless these assets are transferred by dividend or otherwise to us. The ability of our subsidiaries to
pay dividends or otherwise transfer assets to us is subject to various restrictions under applicable law. In addition, our right to receive assets of any of our subsidiaries upon their bankruptcy, liquidation or reorganization, and therefore the
right of the holders of the notes to participate in those assets, will be structurally subordinated to the claims of that subsidiary&#146;s creditors. As of June&nbsp;30, 2021, our subsidiaries had approximately $2.75&nbsp;billion of total
liabilities (excluding intercompany liabilities) outstanding, including trade payables. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B><I>Quanta Services, Inc. is a holding company, and it may not
have access to the cash flow and other assets of its subsidiaries that may be needed to make payments on the notes. </I></B></P> <P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Quanta
Services, Inc. is a holding company and it conducts substantially all of its operations through its subsidiaries. Consequently, it does not have any income from operations and does not expect to generate income from operations in the future. As a
result, its ability to meet its debt service obligations, including its obligations under the notes, substantially depends upon its subsidiaries&#146; earnings, cash flows and business considerations and payment of funds to it by its subsidiaries as
dividends, loans, advances or other payments. In addition, the payment of dividends or the making of loans, advances or other payments to Quanta Services, Inc. may be subject to regulatory or contractual restrictions. The right of Quanta Services,
Inc. to receive any assets of any of its subsidiaries upon their liquidation or reorganization, and therefore the right of the holders of the notes to participate in the profits or a distribution of those assets, will be structurally subordinated to
the claims of that subsidiary&#146;s creditors, including trade creditors. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B><I>The agreements governing our debt, including our existing credit
facility, contain various covenants that impose restrictions on us that may affect our ability to operate our business and to make payments on the notes. </I></B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The agreements governing our existing debt impose, and future financing agreements may impose, operating and financial restrictions on our
activities. These restrictions require us to comply with or maintain certain financial tests and ratios and limit our ability to: </P> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="4%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">incur additional debt and issue preferred stock (in the case of the existing credit facility, but not in the case
of the indenture governing the notes, except for the incurrence of certain secured debt); </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="4%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">redeem or prepay certain debt (in the case of the existing credit facility, but not in the case of the indenture
governing the notes); </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="4%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">pay dividends on our stock or repurchase stock (in the case of the existing credit facility, but not in the case
of the indenture governing the notes); </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="4%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">make certain acquisitions (in the case of the existing credit facility, but not in the case of the indenture
governing the notes); and </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="4%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">engage in consolidations, mergers and acquisitions. </P></TD></TR></TABLE>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">S-13 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">These restrictions on our ability to operate our business could seriously harm our business
by, among other things, limiting our ability to take advantage of financing, merger and acquisition, tax and other corporate opportunities. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Various risks, uncertainties and events beyond our control could affect our ability to comply with these covenants and maintain these
financial tests and ratios. Failure to comply with any of the covenants in our existing or future financing agreements could result in a default under those agreements and under other agreements containing cross-default provisions. A default would
permit lenders to accelerate the maturity for the debt under these agreements and to foreclose upon any collateral securing the debt. Under these circumstances, we might not have sufficient funds or other resources to satisfy all of our obligations,
including our obligations under the notes. In addition, the limitations imposed by financing agreements on our ability to incur additional debt and to take other actions might significantly impair our ability to obtain other financing. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B><I>The limited covenants in the indenture governing the notes may not provide protection against some events or developments that may affect the trading
prices for the notes or our ability to repay the notes. </I></B></P> <P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The indenture governing the notes does not: </P>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="4%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">require us to maintain any financial ratios or specific levels of net worth, revenues, income, cash flow or
liquidity and, accordingly, does not protect holders of the notes in the event that we experience significant adverse changes in our financial condition or results of operations; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="4%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">limit our ability to incur indebtedness that is equal in right of payment to the notes; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="4%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">prohibit us from incurring substantial secured indebtedness that would effectively rank senior to the notes to
the extent of the value of the assets securing the indebtedness; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="4%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">limit our subsidiaries&#146; ability to incur indebtedness, which would rank senior to the notes, except for
limitations on the incurrence of certain secured debt by Restricted Subsidiaries (as such term is defined in the indenture governing the notes); </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="4%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">restrict our subsidiaries&#146; ability to issue securities or otherwise incur indebtedness that would be senior
to our equity interests in our subsidiaries; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="4%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">restrict our ability to repurchase or prepay our securities; or </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="4%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">restrict our ability to make investments or to repurchase or pay dividends or make other payments in respect of
our common stock or other securities ranking junior to the notes. </P></TD></TR></TABLE> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Furthermore, none of our joint ventures or
subsidiaries that are not Restricted Subsidiaries are subject to the restrictive covenants in the notes or in the indenture governing the notes. For these reasons, you should not consider the covenants in the indenture governing the notes as a
significant factor in evaluating whether to invest in the notes. In addition, we are subject to periodic review by independent credit rating agencies. An increase in the level of our outstanding indebtedness, or other events that could have an
adverse impact on our business, properties, financial condition, results of operations or prospects, may cause the rating agencies to downgrade our debt credit rating generally, and the credit ratings on the notes, which could adversely impact the
trading prices for, or the liquidity of, the notes. Any such downgrade could also adversely affect our cost of borrowing, limit our access to the capital markets or result in more restrictive covenants in future debt agreements. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B><I>We may not be able to purchase the outstanding notes upon a Change of Control Triggering Event. </I></B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Upon the occurrence of a &#147;Change of Control Triggering Event&#148; (as defined in &#147;Description of Notes&#151;Purchase upon a Change
of Control Triggering Event&#148;), unless we have exercised our right to redeem such notes in full as described under &#147;Description of Notes&#151;Optional Redemption,&#148; each holder of notes of each series will have the right to require us
to purchase all or any part of such holder&#146;s outstanding notes of such series at a price equal to 101% of their principal amount, plus accrued and unpaid interest, if any, to, but excluding, the date of
</P>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">S-14 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman">
purchase. If we experience a Change of Control Triggering Event, there can be no assurance that we would have sufficient financial resources available to satisfy our obligations to purchase the
notes. In addition, our ability to purchase the notes for cash may be limited by law or the terms of other agreements relating to our indebtedness outstanding at the time. Our failure to purchase the notes of any series as required under the terms
of the notes of such series would result in a default under the notes of such series, which could have material adverse consequences for us and the holders of the notes of such series. See &#147;Description of Notes&#151;Purchase upon a Change of
Control Triggering Event.&#148; </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B><I>If the Blattner Acquisition is not consummated prior to a Special Mandatory Redemption Event, we will be required
to redeem the notes and you may not obtain your expected return on the notes. </I></B></P> <P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Our ability to close the Blattner Acquisition is
subject to the satisfaction of various closing conditions, many of which are beyond our control. Therefore, we may not be able to close the Blattner Acquisition. In the event that (x) the Blattner Acquisition is not consummated on or prior to June
30, 2022 or (y) the Merger Agreement is terminated without the Blattner Acquisition being consummated, we will be required to redeem all of the outstanding 2024 notes, 2032 notes and 2041 notes at a redemption price equal to 101% of the aggregate
principal amount of the 2024 notes, 2032 notes and 2041 notes, respectively, then outstanding, plus accrued and unpaid interest thereon, if any, to (but excluding) the redemption date. If we redeem the notes pursuant to these redemption provisions,
you may not obtain your expected return on the notes and may not be able to reinvest the proceeds from such redemption in an investment that results in a comparable return. In addition, as a result of the special redemption provisions, the trading
prices of the notes may not reflect the financial results of our business or macroeconomic factors. You will have no rights under the special mandatory redemption provisions as long as the Blattner Acquisition is consummated prior to a Special
Mandatory Redemption Event (as defined in &#147;Description of Notes&#148;), nor will you have any right to require us to repurchase your notes if, between the closing of this offering and the consummation of the Blattner Acquisition, we experience
any changes (including any material changes) in our business or financial condition, or if the terms of the Blattner Acquisition or the related transactions change, even if such changes are material and adverse. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B><I>We will not deposit the net proceeds of this offering into an escrow account, and we may not be able to raise the funds necessary to finance the special
mandatory redemption required under certain circumstances by the indenture governing the notes. </I></B></P> <P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">In the event that (x) the Blattner
Acquisition is not consummated on or prior to June 30, 2022 or (y) the Merger Agreement is terminated without the Blattner Acquisition being consummated, we will be required to redeem all of the notes then outstanding. We will not deposit the net
proceeds of this offering into an escrow account pending the closing of the Blattner Acquisition for the purpose of redeeming the notes offered hereby if the Blattner Acquisition is not consummated prior to a Special Mandatory Redemption Event. Our
ability to pay the redemption price to holders of notes following a special mandatory redemption may be limited by our then-existing financial resources, and sufficient funds may not be available when necessary to make any required purchases of the
notes. Any failure to redeem any of the notes pursuant to the special mandatory redemption provisions would constitute a default under the indenture governing the notes. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B><I>Our credit ratings may not reflect all risks of your investment in the notes. </I></B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The credit ratings assigned to the notes are limited in scope, and do not address all material risks relating to an investment in the notes,
but rather reflect only the view of each rating agency on certain matters at the time the credit rating is issued. An explanation of the significance of such credit rating may be obtained from such rating agency. There can be no assurance that such
credit ratings will remain in effect for any given period of time or that a credit rating will not be lowered, suspended or withdrawn entirely by the applicable rating agency if, in such rating agency&#146;s judgment, circumstances so warrant.
Agency credit ratings are not a recommendation to buy, sell or hold any security. Each agency&#146;s credit rating should be evaluated independently of any other agency&#146;s credit rating. Actual or anticipated changes or downgrades in our credit
ratings, including any announcement that our credit ratings are under further review for a downgrade, could adversely affect the market value or liquidity of the notes and increase our corporate borrowing costs. </P>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">S-15 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B><I>An active trading market for the notes may not develop or be sustained. </I></B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The notes are new issues of securities with no established trading market. We do not intend to apply for the listing of the notes on any
securities exchange or for quotation of the notes on any automated dealer quotation system. Although the underwriters have advised us that they presently intend to make a market in the notes after completion of the offering as permitted by
applicable law, they have no obligation to do so, and such market-making activities may be discontinued at any time without notice. In addition, the liquidity of the trading market of the notes and the market price quoted for the notes may be
adversely affected by changes in the overall market for securities and by changes in our financial performance or prospects or the financial performance or prospects of companies in our industry. We cannot assure the liquidity of the trading markets
for the notes or that active public trading markets for the notes will develop or be sustained. If active public trading markets for the notes are not developed or sustained, the market prices and liquidity of the notes may be adversely affected.
</P> <P STYLE="margin-top:12pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B><I>The market prices of the notes may be volatile. </I></B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The market prices of the notes will depend on many factors, including, but not limited to, the following: </P>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="4%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">ratings on our debt securities assigned by rating agencies; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="4%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the time remaining until maturity of the notes; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="4%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the prevailing interest rates being paid by other companies similar to us; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="4%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">our results of operations, financial condition and prospects; and </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="4%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the condition of the financial markets. </P></TD></TR></TABLE>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The condition of the financial markets and prevailing interest rates have fluctuated in the past and are likely to fluctuate in the future,
which could have an adverse effect on the market prices of the notes. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B><I>Redemption may adversely affect your return on the notes. </I></B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">We may redeem all or a portion of the notes at our option at any time or from time to time at the applicable redemption price in the
circumstances described in this prospectus. If we redeem the notes in such circumstances, you may not be able to reinvest the redemption proceeds in securities offering a comparable yield. See &#147;Description of Notes&#151;Optional
Redemption.&#148; </P> <P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B>Risks Relating to the Blattner Acquisition </B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B><I>The pending Blattner Acquisition may not be completed on the currently contemplated timeline or terms, or at all. </I></B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Neither we nor Blattner can provide assurance that the conditions to completing the Blattner Acquisition will be satisfied or waived, and
accordingly, that the Blattner Acquisition will be completed on the terms or timeline that the parties anticipate or at all. If any condition to the Blattner Acquisition is not satisfied, it could delay or prevent the Blattner Acquisition from
occurring, which could negatively impact our business, financial condition, results of operations and growth prospects. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B><I>We may not realize the
anticipated benefits and synergies from the pending Blattner Acquisition. </I></B></P> <P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">While we and Blattner will continue to operate
independently until the completion of the Blattner Acquisition, the success of the Blattner Acquisition will depend, in part, on our ability to realize the anticipated benefits from successfully integrating Blattner&#146;s business. We plan on
devoting substantial management attention and resources to integrating our and Blattner&#146;s business practices and operations so that we can fully realize the anticipated benefits of the Blattner Acquisition. Nonetheless, the business and assets
acquired may not be successful, achieve the anticipated financial results or continue to grow at the same rate as when operated independently or may require greater resources and investments than originally anticipated. The Blattner
</P>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">S-16 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman">
Acquisition could also result in the assumption of unknown or contingent liabilities. Potential difficulties we may encounter in the integration process include the following: </P>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="4%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the inability to successfully integrate Blattner&#146;s business in a manner that permits us to achieve the
strategic operational benefits, additional opportunities with customers, reputational benefits or cost savings anticipated to result from the Blattner Acquisition, which would result in some anticipated benefits of the Blattner Acquisition not being
realized in the time frame currently anticipated, or at all; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="4%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the failure to integrate operations and internal systems, programs and controls; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="4%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the inability to successfully realize the anticipated value from some of Blattner&#146;s assets;
</P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="4%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">lost revenues and lost or damaged commercial relationships; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="4%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the complexities associated with managing the combined company, including difficulties associated with our
decentralized management structure; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="4%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the additional complexities of integrating a business with a different customer base, markets, history, culture
and strategy; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="4%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the failure to retain key employees of either of the two companies that may be difficult to replace;
</P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="4%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the disruption of each company&#146;s ongoing businesses or inconsistencies in services, standards, controls,
procedures and policies; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="4%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">potential unknown liabilities and unforeseen increased expenses, delays or regulatory conditions associated with
the Blattner Acquisition; and </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="4%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">performance shortfalls as a result of the diversion of management&#146;s attention caused by completing the
Blattner Acquisition and integrating Blattner&#146;s operations. </P></TD></TR></TABLE> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Any of these risks could adversely affect our ability
to maintain our commercial relationships and relationships with employees. As a result, the anticipated benefits of the Blattner Acquisition may not be realized fully within the expected timeframe or at all or may take longer to realize or cost more
than expected, which could adversely affect our business, financial condition, results of operations and growth prospects. In addition, changes in laws and regulations could adversely impact our business, financial condition, results of operations
and growth prospects after the Blattner Acquisition. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B><I>We expect to incur substantial expenses related to the Blattner Acquisition. </I></B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">We expect to incur substantial expenses in completing the Blattner Acquisition and integrating the business, operations, practices, policies
and procedures of Blattner. While we assumed that a certain level of transaction and integration expenses would be incurred, there are a number of factors beyond our and Blattner&#146;s control that could affect the total amount or the timing of
their integration expenses. Many of the expenses that will be incurred, by their nature, are difficult to estimate accurately at the present time. The expenses in connection with the Blattner Acquisition are expected to be significant, although the
aggregate amount and timing of such charges are uncertain at present. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B><I>Failure to complete the pending Blattner Acquisition could have an adverse
effect on us. </I></B></P> <P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Either we or Blattner may terminate the Merger Agreement in specified circumstances. If the Blattner Acquisition is
not completed, our business, financial condition, results of operations and growth prospects may be adversely affected and, without realizing any of the benefits of having completed the Blattner Acquisition, we will be subject to a number of risks,
including the following: </P> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="4%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the market price of our securities could decline; </P></TD></TR></TABLE>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">S-17 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">

<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="4%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">we will be required to pay our costs relating to the Blattner Acquisition, such as legal, accounting, financial
advisor, filing and integration costs that have already been incurred or will continue to be incurred until the closing of the Blattner Acquisition, whether or not the Blattner Acquisition is completed; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="4%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">if the Merger Agreement is terminated and our board of directors seeks another acquisition, our stockholders
cannot be certain that we will be able to find another party willing to enter into a transaction as attractive to us as the Blattner Acquisition; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="4%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">we could be subject to litigation related to any failure to complete the Blattner Acquisition or related to any
enforcement proceeding commenced against us to perform our obligations under the Merger Agreement; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="4%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">we will not realize the benefit of the time and resources, financial and otherwise, committed by our management
to matters relating to the Blattner Acquisition that could have been devoted to pursuing other beneficial opportunities; and </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="4%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">we may experience reputational harm due to the adverse perception of any failure to successfully complete the
Blattner Acquisition or negative reactions from the financial markets or from our tenants, managers, vendors, employees and other commercial relationships. </P></TD></TR></TABLE>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Any of these risks could adversely affect our business, financial condition, results of operations and growth prospects. Similarly, delays in
the completion of the Blattner Acquisition could, among other things, result in additional transaction costs, loss of revenue or other negative effects associated with delay and uncertainty about completion of the Blattner Acquisition and could
adversely affect our business, financial condition, results of operations and growth prospects. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B><I>The pendency of the Blattner Acquisition could
adversely affect our and/or Blattner&#146;s businesses and operations. </I></B></P> <P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">In connection with the pending Blattner Acquisition, some
parties with commercial relationships with both us and Blattner may delay or defer decisions, which could adversely affect the revenues, earnings, funds from operations, cash flows and expenses of us and Blattner, regardless of whether the Blattner
Acquisition is completed. Similarly, current and prospective employees of us and Blattner may experience uncertainty about their future roles with the combined company following the Blattner Acquisition, which may adversely affect the ability of
each of us and Blattner to attract and retain key personnel during the pendency of the Blattner Acquisition. In addition, due to operating covenants in the Merger Agreement, Blattner may be unable (without our prior written consent), during the
pendency of the Blattner Acquisition, to pursue strategic transactions, undertake significant capital projects, undertake certain significant financing transactions and otherwise pursue other actions, even if such actions would prove beneficial. We
are subject to a more limited set of operating covenants that may limit or restrict our ability to act in certain circumstances. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B><I>Future
acquisitions and expansions, including the Blattner Acquisition, may increase substantially the level of our contingent liabilities, and we may be unable to integrate them effectively into our existing operations. </I></B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">We evaluate and acquire assets and businesses that we believe complement or diversify our existing assets and businesses. Acquisitions and
business expansions, including the Blattner Acquisition, may require substantial capital. If we consummate the Blattner Acquisition or any future material acquisitions, our capitalization and results of operations may change significantly.
Acquisitions and business expansions, including the Blattner Acquisition, involve numerous risks, including difficulties in the assimilation of the assets and operations of the acquired businesses, inefficiencies and difficulties that arise because
of unfamiliarity with new assets, new geographic areas and the businesses associated with them. Further, unexpected costs and challenges may arise whenever we integrate a business with different operations or employees, and we may experience
unanticipated delays in realizing the benefits of an acquisition, including the Blattner Acquisition. </P>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">S-18 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Following the Blattner Acquisition, we may discover previously unknown liabilities
associated with the acquired business for which we have no recourse under applicable indemnification provisions, if any. In addition, the terms of an acquisition, including the Blattner Acquisition, may require us to assume certain prior known or
unknown liabilities for which we may not be indemnified or have adequate insurance. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B><I>We are not providing pro forma financial statements reflecting
the impact of the Blattner Acquisition on our historical financial information or separate historical financial statements of Blattner. </I></B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">We are not in a position at this time to include pro forma financial information reflecting the estimated pro forma impact of the Blattner
Acquisition on our historical financial information in this prospectus supplement or to include separate financial statements for Blattner. As a result, investors will be required to determine whether to participate in this offering without the
benefit of this financial information. The financial information regarding Blattner we have presented in this prospectus supplement has been prepared based on information made available to us by Blattner, and neither our nor Blattner&#146;s
independent registered public accounting firm expresses an opinion or provides any other form of assurance with respect to the financial or operational information of Blattner included herein. As a result, the financial information with respect to
Blattner included in our future financial statements or in any future public filings may differ materially from the information we have disclosed in connection with this offering. </P>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">S-19 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center"><B><A NAME="supprom326517_6"></A>USE OF PROCEEDS </B></P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">We intend to use the net proceeds from this offering, together with borrowings under our term loan facility, as well as borrowings under our
revolving credit facility or cash on hand, or a combination thereof, if necessary, to finance the cash portion of the consideration for the Blattner Acquisition. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">As of the date of this prospectus supplement, we also have available, but do not expect to utilize, up to $2,183.5 million of committed
financing under the Bridge Facility. In the event that the Bridge Facility is funded prior to completion of this offering, we will be required to use the net proceeds of this offering to prepay the amounts outstanding under the Bridge Facility on a <FONT
STYLE="white-space:nowrap"><FONT STYLE="white-space:nowrap">dollar-for-dollar</FONT></FONT> basis. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">If the Blattner Acquisition is not
consummated prior to a Special Mandatory Redemption Event, we intend to use the net proceeds from the notes, together with borrowings under our revolving credit facility or cash on hand, or a combination thereof, if necessary, to fund the special
mandatory redemption of the notes described in &#147;Description of Notes&#151;Special Mandatory Redemption.&#148; </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Affiliates of BofA
Securities, Inc. and Wells Fargo Securities LLC have provided commitments under the Bridge Facility. In the event that the Bridge Facility is funded prior to completion of this offering, we will be required to use the net proceeds of this offering
to prepay the amounts outstanding under the Bridge Facility on a <FONT STYLE="white-space:nowrap"><FONT STYLE="white-space:nowrap">dollar-for-dollar</FONT></FONT> basis. As such, at least 5% or more of the net proceeds of this offering (not
including underwriting discounts) may be directed to one or more of the underwriters or their affiliates. The receipt of at least 5% of the net proceeds of this offering by any underwriter (or its affiliates) would be considered a &#147;conflict of
interest&#148; under FINRA Rule 5121 regarding the underwriting of securities of a company with a member that has a conflict of interest within the meaning of those rules. Pursuant to that rule, the appointment of a &#147;qualified independent
underwriter&#148; (as such term is defined in FINRA Rule 5121) is not necessary in connection with this offering as the securities offered are investment grade rated, as that term is defined in the rule. In accordance with FINRA Rule 5121, the
underwriters with a conflict of interest will not confirm sales of notes to any account over which they exercise discretionary authority without prior written approval of the customer. See &#147;Underwriting (Conflicts of Interest).&#148; </P>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">S-20 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center"><B><A NAME="supprom326517_7"></A>CAPITALIZATION </B></P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The following table sets forth our consolidated cash and cash equivalents and our capitalization as of June&nbsp;30, 2021: </P>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="4%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">on an actual basis; and </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="4%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">on an as adjusted basis to give effect to the sale of the notes offered hereby, the application of the proceeds
therefrom in the manner described under &#147;Use of Proceeds&#148; and the financing of the remainder of the cash portion of the consideration for the Blattner Acquisition in the manner described under &#147;Use of Proceeds,&#148; assuming that the
amount of such cash consideration, which will be determined at the closing of the Merger, will total approximately $2.36 billion. </P></TD></TR></TABLE>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">In addition to the section &#147;Use of Proceeds,&#148; you should read the data set forth in the table below in conjunction with
&#147;Management&#146;s Discussion and Analysis of Financial Condition and Results of Operations&#148; and our historical condensed consolidated financial statements and related notes included in our Q2 Quarterly Report, each of which is
incorporated by reference in this prospectus supplement and the accompanying prospectus. </P> <P STYLE="font-size:12pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE CELLSPACING="0" CELLPADDING="0" WIDTH="76%" BORDER="0" STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:9pt" ALIGN="center">


<TR>

<TD WIDTH="70%"></TD>

<TD VALIGN="bottom" WIDTH="6%"></TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TD VALIGN="bottom" WIDTH="6%"></TD>
<TD></TD>
<TD></TD>
<TD></TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:8pt">
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="bottom" COLSPAN="6" ALIGN="center" STYLE="border-bottom:1.00pt solid #000000"><B>As of June&nbsp;30, 2021</B></TD>
<TD VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:8pt">
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="bottom" COLSPAN="2" ALIGN="center" STYLE="border-bottom:1.00pt solid #000000"><B>Actual</B></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="bottom" COLSPAN="2" ALIGN="center" STYLE="border-bottom:1.00pt solid #000000"><B>As&nbsp;adjusted</B></TD>
<TD VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:8pt">
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="bottom" COLSPAN="6" ALIGN="center"><B>(in thousands)</B></TD>
<TD VALIGN="bottom">&nbsp;</TD></TR>


<TR BGCOLOR="#cceeff" STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:9pt; font-family:Times New Roman">Cash and cash equivalents</P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom"><FONT STYLE="font-size:9pt">$</FONT></TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right"><FONT STYLE="font-size:9pt">212,473</FONT></TD>
<TD NOWRAP VALIGN="bottom"><FONT STYLE="font-size:9pt">&nbsp;</FONT></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom"><FONT STYLE="font-size:9pt">$</FONT></TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right"><FONT STYLE="font-size:9pt">212,473</FONT></TD>
<TD NOWRAP VALIGN="bottom"><FONT STYLE="font-size:9pt">(a)&nbsp;</FONT></TD></TR>
<TR STYLE="font-size:1px; ">
<TD VALIGN="bottom"></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:3.00px double #000000">&nbsp;</P></TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:3.00px double #000000">&nbsp;</P></TD>
<TD>&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:3.00px double #000000">&nbsp;</P></TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:3.00px double #000000">&nbsp;</P></TD>
<TD>&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:9pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:9pt; font-family:Times New Roman">Revolving credit facility (b)(c)</P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">323,281</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">449,983</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR BGCOLOR="#cceeff" STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:9pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:9pt; font-family:Times New Roman">Term loan facility (c)(d)</P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">&#151;&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">750,000</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:9pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:9pt; font-family:Times New Roman">2.900% senior notes due 2030 (e)</P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">987,771</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">987,771</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR BGCOLOR="#cceeff" STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:9pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:9pt; font-family:Times New Roman">Senior notes due 2024 offered hereby (e)</P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">&#151;&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">496,686</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:9pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:9pt; font-family:Times New Roman">Senior notes due 2032 offered hereby (e)</P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">&#151;&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">495,151</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR BGCOLOR="#cceeff" STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:9pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:9pt; font-family:Times New Roman">Senior notes due 2041 offered hereby (e)</P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">&#151;&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">491,731</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:9pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:9pt; font-family:Times New Roman">Other long-term debt</P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">51,254</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">51,254</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR BGCOLOR="#cceeff" STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:9pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:9pt; font-family:Times New Roman">Finance leases</P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">2,412</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">2,412</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="font-size:1px; ">
<TD VALIGN="bottom"></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD>&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD>&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:9pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:9pt; font-family:Times New Roman">Total long-term debt </P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">1,364,718</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">3,724,988</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="font-size:1px; ">
<TD VALIGN="bottom"></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD>&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD>&nbsp;</TD></TR>
<TR BGCOLOR="#cceeff" STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:9pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:9pt; font-family:Times New Roman">Total stockholders&#146; equity</P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">4,486,732</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">4,486,732</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="font-size:1px; ">
<TD VALIGN="bottom"></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD>&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD>&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:9pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:9pt; font-family:Times New Roman">Total capitalization</P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">5,851,450</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">8,211,720</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="font-size:1px; ">
<TD VALIGN="bottom"></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:3.00px double #000000">&nbsp;</P></TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:3.00px double #000000">&nbsp;</P></TD>
<TD>&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:3.00px double #000000">&nbsp;</P></TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:3.00px double #000000">&nbsp;</P></TD>
<TD>&nbsp;</TD></TR>
</TABLE> <P STYLE="line-height:8.0pt;margin-top:0pt;margin-bottom:2pt;border-bottom:1px solid #000000;width:11%">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%" VALIGN="top" ALIGN="left">(a)</TD>
<TD ALIGN="left" VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman; " ALIGN="left">The as adjusted cash and cash equivalents amount assumes that the remainder of the cash portion of the
consideration for the Blattner Acquisition is financed with borrowings under our revolving credit facility. The actual amount of cash and cash equivalents may be lower in the event we decide to use cash on hand to finance the remainder of such cash
consideration. The as adjusted cash and cash equivalents amount also does not give effect to any transaction costs or expenses to be incurred by the Company in connection with the Blattner Acquisition. </P></TD></TR></TABLE>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%" VALIGN="top" ALIGN="left">(b)</TD>
<TD ALIGN="left" VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman; " ALIGN="left">As of June&nbsp;30, 2021, we had approximately $301.6&nbsp;million of outstanding letters of credit and
approximately $1.89&nbsp;billion of unused availability under our revolving credit facility. As of September 3, 2021, we had approximately $324.2 million of outstanding letters of credit and approximately $1.80 billion of unused availability under
our revolving credit facility. The as adjusted borrowings give effect to the credit agreement amendment we expect to enter into prior to consummation of the Blattner Acquisition and assume that $126.7&nbsp;million of borrowings are incurred under
the revolving credit facility to finance the remainder of the cash portion of the consideration for the Blattner Acquisition. The actual amount of such borrowings may be lower to the extent we decide to use cash on hand to finance the remainder of
such cash consideration. </P></TD></TR></TABLE>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%" VALIGN="top" ALIGN="left">(c)</TD>
<TD ALIGN="left" VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman; " ALIGN="left">The credit agreement amendment is being negotiated as of the date of this prospectus supplement and its
effectiveness therefore remains subject to market conditions and the satisfaction of certain conditions precedent, and there are no assurances that we will enter into the credit agreement amendment on the terms described herein, including with
respect to the size of the term loan facility, or at all; if we enter into the credit agreement amendment, we will not be obligated to make any borrowings thereunder. </P></TD></TR></TABLE>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">S-21 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">

<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%" VALIGN="top" ALIGN="left">(d)</TD>
<TD ALIGN="left" VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman; " ALIGN="left">In connection with this offering, after giving effect to the credit agreement amendment we expect to enter into
prior to consummation of the Blattner Acqusition, we intend to incur borrowings under our new term loan facility to partially finance the cash portion of the consideration for the Blattner Acquisition. This offering is not conditioned upon the
incurrence of new term loan borrowings. If the Blattner Acquisition does not close, we do not expect to draw upon our new term loan facility. </P></TD></TR></TABLE>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%" VALIGN="top" ALIGN="left">(e)</TD>
<TD ALIGN="left" VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman; " ALIGN="left">Net of unamortized discounts and estimated debt issuance costs. </P></TD></TR></TABLE>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">S-22 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center"><B><A NAME="supprom326517_8"></A>DESCRIPTION OF NOTES </B></P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The following description of the particular terms of the notes offered hereby (referred to in the accompanying prospectus as &#147;debt
securities&#148;) supplements and, to the extent inconsistent therewith, supersedes the description of the general terms and provisions of debt securities set forth in the accompanying prospectus. Capitalized terms not otherwise defined herein shall
have the meanings given to them in the accompanying prospectus. In this description, all references to the &#147;Company,&#148; &#147;we,&#148; &#147;us&#148; and &#147;our&#148; refer only to Quanta Services, Inc. and not to any of its
subsidiaries. Unless otherwise indicated or unless the context requires otherwise, references to the &#147;notes&#148; refer to the 2024 notes, the 2032 notes and the 2041 notes, and references to the &#147;indenture&#148; governing the notes refer
to the base indenture (as defined below) as supplemented by the second supplemental indenture (as defined below), the third supplemental indenture (as defined below) and the fourth supplemental indenture (as defined below), respectively. </P>
<P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B>General </B></P> <P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The 2024 notes will be issued
under the indenture, dated as of September&nbsp;22, 2020 (the &#147;base indenture&#148;), between the Company and U.S. Bank National Association, as trustee (the &#147;Trustee&#148;), as to be supplemented and amended by the second supplemental
indenture, dated as of September&nbsp;23, 2021 (the &#147;second supplemental indenture&#148;), between the Company and the Trustee. The 2032 notes will be issued under the base indenture as to be supplemented and amended by the third supplemental
indenture, dated as of September&nbsp;23, 2021 (the &#147;third supplemental indenture&#148;), between the Company and the Trustee. The 2041 notes will be issued under the base indenture as to be supplemented and amended by the fourth supplemental
indenture, dated as of September&nbsp;23, 2021 (the &#147;fourth supplemental indenture&#148;), between the Company and the Trustee. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The
indenture is subject to and is governed by the Trust Indenture Act of 1939, as amended (the &#147;Trust Indenture Act&#148;), and the terms of the notes include those made part of the indenture by reference to the Trust Indenture Act. The following
description and the description in the accompanying prospectus do not purport to be complete and are subject to and qualified in their entirety by reference to the Trust Indenture Act and all the provisions of the notes and the indenture. We urge
you to read the indenture because it, and not this description, defines your rights as a holder of the notes. </P> <P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B>Principal Amount and Maturity </B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">We are offering $500,000,000 aggregate principal amount of senior notes due 2024 (the &#147;2024 notes&#148;). The 2024 notes will mature on
October&nbsp;1, 2024. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">We are offering $500,000,000 aggregate principal amount of senior notes due 2032 (the &#147;2032 notes&#148;). The
2032 notes will mature on January&nbsp;15, 2032. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">We are offering $500,000,000 aggregate principal amount of senior notes due 2041 (the
&#147;2041 notes&#148;). The 2041 notes will mature on October&nbsp;1, 2041. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The Company may, without notice to or consent of the holders
or beneficial owners of the notes, issue in separate offerings additional notes of each series having the same ranking, interest rate, maturity and other terms (except the issue date, price to the public and, if applicable, the initial interest
payment date) as the notes of such series. The notes of such series and any additional notes of such series will constitute a separate series under the indenture. If any such additional notes of any series are not fungible with the notes of such
series for U.S. federal income tax purposes, such additional notes will be issued with a different CUSIP number (or other applicable identifying number). </P>
<P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B>Interest </B></P> <P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Except as otherwise provided in
the indenture, interest on the 2024 notes will accrue at a rate of 0.950% per annum from September&nbsp;23, 2021 and will be payable semi-annually in arrears on April&nbsp;1 and October&nbsp;1, </P>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">S-23 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman">
commencing April&nbsp;1, 2022, to those persons in whose names the 2024 notes are registered at the close of business on the next preceding March&nbsp;15 and September&nbsp;15, whether or not a
business day, as the case may be. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Except as otherwise provided in the indenture, interest on the 2032 notes will accrue at a rate of
2.350% per annum from September&nbsp;23, 2021 and will be payable semi-annually in arrears on January&nbsp;15 and July&nbsp;15, commencing July&nbsp;15, 2022, to those persons in whose names the 2032 notes are registered at the close of business on
the next preceding January&nbsp;1 and July&nbsp;1, whether or not a business day, as the case may be. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Except as otherwise provided in the
indenture, interest on the 2041 notes will accrue at a rate of 3.050% per annum from September&nbsp;23, 2021 and will be payable semi-annually in arrears on April&nbsp;1 and October&nbsp;1, commencing April&nbsp;1, 2022, to those persons in whose
names the 2041 notes are registered at the close of business on the next preceding March&nbsp;15 and September&nbsp;15, whether or not a business day, as the case may be. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">If any interest payment date, any redemption date, the maturity date or any other date on which the principal of or premium, if any, or
interest on a note becomes due and payable falls on a day that is not a business day, the required payment shall be made on the next business day as if it were made on the date the payment was due, and no interest shall accrue on the amount so
payable for the period from and after the interest payment date, redemption date, maturity date or other date, as the case may be. </P> <P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B>Ranking </B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The notes (i)&nbsp;will be the Company&#146;s senior unsecured obligations, (ii)&nbsp;will rank equally in right of payment with all of the
Company&#146;s existing and future senior unsecured indebtedness, subject to applicable law, (iii)&nbsp;will be senior in right of payment to all of the Company&#146;s future subordinated indebtedness, if any, subject to applicable law,
(iv)&nbsp;will be effectively subordinated to the Company&#146;s secured indebtedness, if any, to the extent of the value of the assets securing such indebtedness and (v)&nbsp;will be structurally subordinated to all liabilities, including trade
payables, of any of the Company&#146;s subsidiaries. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">As of June&nbsp;30, 2021, as adjusted for this offering, the application of the net
proceeds therefrom as set forth in &#147;Use of Proceeds&#148; and an assumed amount of $750 million in borrowings under our new term loan facility (after giving effect to the credit agreement amendment described in &#147;Summary&#151;Recent
Developments&#151;Credit Agreement Amendment,&#148; but prior to potentially financing the remainder of the cash portion of the consideration for the Blattner Acquisition with borrowings under our revolving credit facility as set forth in &#147;Use
of Proceeds&#148;), we would have had approximately $3.60&nbsp;billion of outstanding debt, of which $53.7&nbsp;million would have been secured, and we would have had $1.89&nbsp;billion of undrawn borrowing capacity under our revolving credit
facility. The credit agreement amendment is being negotiated as of the date of this prospectus supplement and its effectiveness therefore remains subject to market conditions and the satisfaction of certain conditions precedent, and there are no
assurances that we will enter into the credit agreement amendment on the terms described herein, including with respect to the size of our term loan facility, or at all; if we enter into the credit agreement amendment, we will not be obligated to
make any borrowings thereunder, but the commitments under the Bridge Facility would be permanently reduced by 100% of the commitments pursuant to our term loan facility as long as the conditions to availability of our term loan facility are no more
restrictive than the Bridge Facility. As of June&nbsp;30, 2021, the Company&#146;s subsidiaries had approximately $2.75&nbsp;billion of total liabilities (excluding intercompany liabilities) outstanding, including trade payables. </P>
<P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B>Special Mandatory Redemption </B></P> <P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">In the
event that (x) the Blattner Acquisition is not consummated on or prior to June 30, 2022 or (y) the Merger Agreement is terminated without the Blattner Acquisition being consummated (any such event being a &#147;Special Mandatory Redemption
Event&#148;), we will redeem all of the 2024 notes, 2032 notes and 2041 notes then outstanding (the &#147;Special Mandatory Redemption&#148;), at a price equal to 101% of the aggregate principal amount of the 2024 notes, 2032 notes and 2041 notes,
respectively, then outstanding, plus accrued and unpaid interest thereon, if any, to (but excluding) the redemption date (the &#147;Special Mandatory Redemption Price&#148;). For </P>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">S-24 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman">
purposes of the foregoing, the Blattner Acquisition will be deemed consummated if the closing under the Merger Agreement occurs, including after giving effect to any amendments to the Merger
Agreement or waivers thereunder acceptable to us. The completion of this offering is not contingent on the consummation of the Blattner Acquisition. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Notice of the occurrence of a Special Mandatory Redemption Event and that a Special Mandatory Redemption is to occur (the &#147;Special
Mandatory Redemption Notice&#148;) will be delivered to the Trustee and delivered to holders of notes according to the procedures of the Depositary within 10 business days after the Special Mandatory Redemption Event. At our written request, the
Trustee shall give the Special Mandatory Redemption Notice in our name and at our expense. On the redemption date specified in the Special Mandatory Redemption Notice, which shall be no more than 10 business days (or such other minimum period as may
be required by the Depositary) after mailing or sending the Special Mandatory Redemption Notice, the special mandatory redemption shall occur (the date of such redemption, the &#147;Special Mandatory Redemption Date&#148;). If funds sufficient to
pay the Special Mandatory Redemption Price of all of the notes of any series then outstanding on the Special Mandatory Redemption Date are deposited with a paying agent or the Trustee on or before such Special Mandatory Redemption Date, then on and
after such Special Mandatory Redemption Date, the notes of such series shall cease to bear interest and, other than the right to receive the Special Mandatory Redemption Price, all rights under the notes of such series shall terminate. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The proceeds of this offering will not be deposited into an escrow account benefitting the holders pending any Special Mandatory Redemption of
the notes. Our ability to pay the redemption price to holders of notes following a Special Mandatory Redemption may be limited by our then-existing financial resources, and sufficient funds may not be available when necessary to make any required
purchases of notes. See &#147;Risk Factors&#151;Risks Relating the Notes&#151;We will not deposit the net proceeds of this offering into an escrow account, and we may not be able to raise the funds necessary to finance the special mandatory
redemption required under certain circumstances by the indenture governing the notes.&#148; </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Upon the consummation of the Blattner
Acquisition, the foregoing provisions regarding the Special Mandatory Redemption will cease to apply. </P> <P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B>Optional Redemption </B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">In addition to as set forth under &#147;&#151;Special Mandatory Redemption&#148; above, the notes will be redeemable, at our option, as set
forth below. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Commencing on October&nbsp;1, 2022, we may redeem the 2024 notes, in whole, or from time to time in part, at our option, at
any time, at a redemption price equal to 100% of the principal amount of the 2024 notes being redeemed <I>plus</I> accrued and unpaid interest, if any, to (but excluding) the redemption date. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Prior to October&nbsp;1, 2022, the 2024 notes will be redeemable, at our option, at any time in whole, or from time to time in part, at a
price equal to the greater of: </P> <P STYLE="margin-top:6pt; margin-bottom:0pt; margin-left:4%; text-indent:4%; font-size:10pt; font-family:Times New Roman">(a) 100% of the principal amount of such 2024 notes to be redeemed; and </P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; margin-left:4%; text-indent:4%; font-size:10pt; font-family:Times New Roman">(b) the sum of the present values of the Remaining Scheduled Payments thereon that would be due if the 2024 notes matured on
the Par Call Date, discounted to the redemption date on a semiannual basis (assuming a <FONT STYLE="white-space:nowrap">360-day</FONT> year consisting of twelve <FONT STYLE="white-space:nowrap">30-day</FONT> months) at the Treasury Rate <I>plus</I>
10&nbsp;basis points, </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><I>plus</I>, in either case, accrued and unpaid interest, if any, on the principal amount being redeemed to (but excluding) the
date of redemption. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Commencing on October&nbsp;15, 2031 (three months prior to their maturity date), we may redeem the 2032 notes, in
whole, or from time to time in part, at our option, at any time, at a redemption price equal to 100% of </P>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">S-25 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman">
the principal amount of the 2032 notes being redeemed <I>plus</I> accrued and unpaid interest, if any, to (but excluding) the redemption date. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Prior to October&nbsp;15, 2031 (three months prior to their maturity date), the 2032 notes will be redeemable, at our option, at any time in
whole, or from time to time in part, at a price equal to the greater of: </P> <P STYLE="margin-top:6pt; margin-bottom:0pt; margin-left:4%; text-indent:4%; font-size:10pt; font-family:Times New Roman">(a) 100% of the principal amount of such 2032
notes to be redeemed; and </P> <P STYLE="margin-top:6pt; margin-bottom:0pt; margin-left:4%; text-indent:4%; font-size:10pt; font-family:Times New Roman">(b) the sum of the present values of the Remaining Scheduled Payments thereon that would be due
if the 2032 notes matured on the Par Call Date, discounted to the redemption date on a semiannual basis (assuming a <FONT STYLE="white-space:nowrap">360-day</FONT> year consisting of twelve <FONT STYLE="white-space:nowrap">30-day</FONT> months) at
the Treasury Rate <I>plus</I> 20&nbsp;basis points, </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><I>plus</I>, in either case, accrued and unpaid interest, if any, on the principal amount being
redeemed to (but excluding) the date of redemption. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Commencing on April&nbsp;1, 2041 (six months prior to their maturity date), we may
redeem the 2041 notes, in whole, or from time to time in part, at our option, at any time, at a redemption price equal to 100% of the principal amount of the 2041 notes being redeemed <I>plus</I> accrued and unpaid interest, if any, to (but
excluding) the redemption date. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Prior to April&nbsp;1, 2041 (six months prior to their maturity date), the 2041 notes will be redeemable,
at our option, at any time in whole, or from time to time in part, at a price equal to the greater of: </P> <P STYLE="margin-top:6pt; margin-bottom:0pt; margin-left:4%; text-indent:4%; font-size:10pt; font-family:Times New Roman">(a) 100% of the
principal amount of such 2041 notes to be redeemed; and </P> <P STYLE="margin-top:6pt; margin-bottom:0pt; margin-left:4%; text-indent:4%; font-size:10pt; font-family:Times New Roman">(b) the sum of the present values of the Remaining Scheduled
Payments thereon that would be due if the 2041 notes matured on the Par Call Date, discounted to the redemption date on a semiannual basis (assuming a <FONT STYLE="white-space:nowrap">360-day</FONT> year consisting of twelve <FONT
STYLE="white-space:nowrap">30-day</FONT> months) at the Treasury Rate <I>plus</I> 20&nbsp;basis points, </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman"><I>plus</I>, in either case,
accrued and unpaid interest, if any, on the principal amount being redeemed to (but excluding) the date of redemption. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The indenture
provides that with respect to any such redemption, the Company will notify the Trustee of the redemption price promptly after the calculation and that the Trustee will not be responsible for such calculation. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">&#147;Comparable Treasury Issue&#148; means the United States Treasury security selected by an Independent Investment Banker as having a
maturity comparable to the remaining term of the notes to be redeemed that would be utilized (assuming for this purpose that the notes matured on the applicable Par Call Date), at the time of selection and in accordance with customary financial
practice, in pricing new issues of corporate debt securities of comparable maturity to the remaining term of such notes. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">&#147;Comparable
Treasury Price&#148; means, with respect to any redemption date, (i)&nbsp;the average of the Reference Treasury Dealer Quotations, after excluding the highest and lowest of such Reference Treasury Dealer Quotations, or (ii)&nbsp;if the Company
obtains fewer than four such Reference Treasury Dealer Quotations, the average of all such Reference Treasury Dealer Quotations. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">&#147;Independent Investment Banker&#148; means one of the Reference Treasury Dealers appointed by the Company. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">&#147;Par Call Date&#148; means: with respect to the 2024 notes, October&nbsp;1, 2022; with respect to the 2032 notes, October&nbsp;15, 2031
(three months prior to their maturity date); and with respect to the 2041 notes, April&nbsp;1, 2041 (six months prior to their maturity date). </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">&#147;Reference Treasury Dealer&#148; means (1)&nbsp;each of BofA Securities, Inc. and Wells Fargo Securities, LLC, and their respective
successors; <I>provided</I>, <I>however</I>, that if any of the foregoing shall cease to be a primary U.S. </P>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">S-26 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman">
Government securities dealer in New York City (a &#147;Primary Treasury Dealer&#148;), the Company shall substitute therefor another Primary Treasury Dealer and (2)&nbsp;any two other nationally
recognized investment banking firms that are Primary Treasury Dealers specified from time to time by the Company. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">&#147;Reference
Treasury Dealer Quotations&#148; means, with respect to each Reference Treasury Dealer and any redemption date, the average, as determined by the Company, of the bid and asked prices for the Comparable Treasury Issue (expressed in each case as a
percentage of its principal amount) quoted in writing to the Company by such Reference Treasury Dealer at 5:00 p.m. New York City time on the third business day preceding such redemption date. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">&#147;Remaining Scheduled Payments&#148; means, with respect to any note, the remaining scheduled payments of the principal thereof to be
redeemed and interest thereon that would be due after the related redemption date but for such redemption (assuming for this purpose that the notes mature on the applicable Par Call Date); provided, however, that, if such redemption date is not an
interest payment date with respect to such notes, the amount of the next succeeding scheduled interest payment thereon will be reduced by the amount of interest accrued thereon to such redemption date. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">&#147;Treasury Rate&#148; means, with respect to any redemption date for the notes, the rate per annum equal to the semiannual equivalent
yield to maturity of the Comparable Treasury Issue (assuming for this purpose that the notes matured on the applicable Par Call Date), assuming a price for the Comparable Treasury Issue (expressed as a percentage of its principal amount) equal to
the Comparable Treasury Price for such redemption date. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Notice of any such optional redemption will be mailed or sent at least 10 days
but not more than 60 days before the redemption date to each holder of notes of such series to be redeemed. Any such redemption of notes or notice thereof may, at the Company&#146;s discretion, be subject to one or more conditions precedent,
including, but not limited to, completion of a corporate transaction that is pending (such as an equity or equity-linked offering, an incurrence of indebtedness or an acquisition or other strategic transaction involving a change of control in us or
another entity). If such redemption is so subject to satisfaction of one or more conditions precedent, such notice shall describe each such condition, and such notice may be rescinded in the event that any or all such conditions shall not have been
satisfied or otherwise waived on or prior to the business day immediately preceding the relevant redemption date. If the Company redeems less than all the notes of such series, the Trustee must select the notes of such series to be redeemed, in the
case of the notes in global form, in accordance with the Depositary&#146;s applicable procedures, and in the case of any notes of such series in definitive form, by such method as the Trustee deems fair and appropriate. The Trustee may select for
partial redemption notes and portions of notes in amounts equal to $2,000 or any integral multiple of $1,000 in excess thereof. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Unless
the Company defaults in payment of the redemption price for notes of such series, on and after the applicable redemption date, interest will cease to accrue on the notes of such series or portions thereof called for redemption. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">In addition, the Company may at any time, and from time to time, purchase notes at any price or prices in the open market, through negotiated
transactions, by tender offer or otherwise, subject to applicable law. </P> <P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B>Purchase upon a Change of Control Triggering Event </B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Upon the occurrence of a Change of Control Triggering Event, unless the Company has exercised its right to redeem the notes of any series in
full as described under &#147;&#151;Optional Redemption&#148; by giving irrevocable notice to the Trustee in accordance with the indenture, each holder of the notes of such series will have the right to require the Company to purchase all or a
portion (equal to $2,000 or whole multiples of $1,000 in excess thereof) of such holder&#146;s notes of such series pursuant to the offer described below (the &#147;Change of Control Offer&#148;) at a purchase price equal to 101% of the principal
amount thereof <I>plus</I> accrued and unpaid interest, if any, to (but excluding) the date of purchase (the &#147;Change of Control Payment&#148;), subject to the rights of holders of such notes </P>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">S-27 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman">
on the relevant record date to receive interest due on the relevant interest payment date. If the Change of Control Payment Date (as defined below) falls on a day that is not a business day, the
related payment of the Change of Control Payment will be made on the next business day as if it were made on the date such payment was due, and no interest will accrue on the amounts so payable for the period from and after such date to the next
business day. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Unless the Company has exercised its right to redeem such notes, within 30 days following the date upon which the Change of
Control Triggering Event occurred with respect to the notes of such series or, at the Company&#146;s option, prior to any Change of Control but after the public announcement of the pending Change of Control, the Company will be required to send, by
first class mail (or with respect to global notes, to the extent permitted or required by applicable procedures or regulations of the Depositary, send electronically) a notice to each holder of such notes, with a copy to the Trustee, which notice
will govern the terms of the Change of Control Offer. The notice will state, among other things, the purchase date, which, other than as may be required by applicable law, must be no earlier than 10 days nor later than 60 days after the date the
notice is mailed or sent (or, in the case of a notice mailed or sent prior to the date of consummation of a Change of Control, no earlier than the date of the occurrence of the Change of Control), other than as may be required by law (the
&#147;Change of Control Payment Date&#148;). The notice, if mailed or sent prior to the date of consummation of the Change of Control, will state that the Change of Control Offer is conditioned on the Change of Control being consummated on or prior
to the Change of Control Payment Date. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">On the Change of Control Payment Date, the Company will, to the extent lawful: </P>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">accept or cause a third party to accept for payment all notes of such series or portions of notes of such series
properly tendered pursuant to the Change of Control Offer; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">deposit or cause a third party to deposit with the paying agent an amount equal to the Change of Control Payment
in respect of all notes of such series or portions of notes of such series properly tendered; and </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">deliver or cause to be delivered to the Trustee the notes of such series properly accepted together with an
officers&#146; certificate or statement signed by an officer of the Company, which need not constitute an officers&#146; certificate, stating the aggregate principal amount of notes of such series or portions of notes of such series being purchased.
</P></TD></TR></TABLE> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The Company will not be required to make a Change of Control Offer with respect to the notes of such series if
(i)&nbsp;a third party makes such an offer in the manner, at the times and otherwise in compliance with the requirements for such an offer made by the Company and such third party purchases all the notes of such series properly tendered and not
withdrawn under the third party&#146;s offer, (ii)&nbsp;a notice of redemption has been given to the holders of all of the notes of such series in accordance with the terms of the indenture, unless and until there is a default in payment of the
redemption price, or (iii)&nbsp;in connection with or in contemplation of any Change of Control, the Company has made an offer to purchase (an &#147;Alternate Offer&#148;) any and all notes of such series validly tendered at a cash price equal to or
higher than the Change of Control Payment and has purchased all notes of such series properly tendered in accordance with the terms of such Alternate Offer. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The Company will comply in all material respects with the requirements of Rule <FONT STYLE="white-space:nowrap">14e-1</FONT> under the
Securities Exchange Act of 1934, as amended (the &#147;Exchange Act&#148;), and any other securities laws and regulations thereunder to the extent those laws and regulations are applicable in connection with the purchase of the notes of such series
as a result of a Change of Control Triggering Event. To the extent that the provisions of any such securities laws or regulations conflict with the Change of Control Offer provisions of the notes of such series, the Company will comply with those
securities laws and regulations and will not be deemed to have breached its obligations under the Change of Control Offer provisions of the notes of such series or the indenture by virtue of any such conflict. </P>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">S-28 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">For purposes of the foregoing discussion of a Change of Control Offer, the following
definitions are applicable: </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">&#147;Change of Control&#148; means the occurrence of any of the following after the date of issuance of the
notes: </P> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="5%" VALIGN="top" ALIGN="left">1.</TD>
<TD ALIGN="left" VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman; " ALIGN="left">the direct or indirect sale, transfer, conveyance or other disposition (other than by way of merger or
consolidation), in one or a series of related transactions, of all or substantially all of the properties or assets of the Company and its Subsidiaries, taken as a whole, to any &#147;person&#148; (as that term is used in Section&nbsp;13(d)(3) of
the Exchange Act) other than to the Company or any of its Subsidiaries, other than any such transaction or series of related transactions where holders of the Company&#146;s Voting Stock outstanding immediately prior thereto hold Voting Stock of the
transferee Person representing a majority of the voting power of the transferee Person&#146;s Voting Stock immediately after giving effect thereto; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="5%" VALIGN="top" ALIGN="left">2.</TD>
<TD ALIGN="left" VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman; " ALIGN="left">the consummation of any transaction the result of which is that a &#147;person&#148; or &#147;group&#148; (as
those terms are used in Section&nbsp;13(d)(3) of the Exchange Act, but excluding any employee benefit plan of such person or its subsidiaries, and any person or entity acting in its capacity as trustee, agent or other fiduciary or administrator of
any such plan) becomes the ultimate &#147;beneficial owner&#148; (as defined in Rule <FONT STYLE="white-space:nowrap">13d-3</FONT> under the Exchange Act) of more than 50% of the total voting power of the Voting Stock of the Company on a fully
diluted basis; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="5%" VALIGN="top" ALIGN="left">3.</TD>
<TD ALIGN="left" VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman; " ALIGN="left">the adoption by the Company&#146;s stockholders of a plan relating to the liquidation or dissolution of the
Company; or </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="5%" VALIGN="top" ALIGN="left">4.</TD>
<TD ALIGN="left" VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman; " ALIGN="left">the Company consolidates with, or merges with or into, any Person, or any Person consolidates with, or merges
with or into the Company, in any such event pursuant to a transaction in which any of the outstanding Voting Stock of the Company or such other Person is converted into or exchanged for cash, securities or other property, other than any such
transaction where (A)&nbsp;the Voting Stock of the Company outstanding immediately prior to such transaction constitutes, or is converted into or exchanged for, Voting Stock of the surviving or transferee Person (or its parent) constituting a
majority of the outstanding shares of such Voting Stock of such surviving or transferee Person (or its parent) (immediately after giving effect to such issuance) and (B)&nbsp;immediately after such transaction, no &#147;person&#148; or
&#147;group&#148; (as those terms are used in Section&nbsp;13(d)(3) of the Exchange Act, but excluding any employee benefit plan of such person or its subsidiaries, and any person or entity acting in its capacity as trustee, agent or other fiduciary
or administrator of any such plan) becomes, directly or indirectly, the &#147;beneficial owner&#148; (as defined in Rule <FONT STYLE="white-space:nowrap">13d-3</FONT> under the Exchange Act) of more than 50% of the voting power of the Voting Stock
of the surviving or transferee Person. </P></TD></TR></TABLE> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Notwithstanding the foregoing, a transaction will not be deemed to involve a
Change of Control solely because the Company shall become a direct or indirect wholly-owned subsidiary of a holding company or other Person if the direct or indirect holders of the Voting Stock of such holding company or other Person immediately
following that transaction are substantially the same as the holders of the Company&#146;s Voting Stock immediately prior to that transaction. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">&#147;Change of Control Triggering Event&#148; means, with respect to any series of notes, (i)&nbsp;the rating of the notes of such series by
both Rating Agencies is lowered at any time during the period (the &#147;Trigger Period&#148;) commencing on the earlier of (a)&nbsp;the occurrence of a Change of Control and (b)&nbsp;the first public announcement by us of any Change of Control (or
pending Change of Control), and ending 60 days following consummation of such Change of Control (which Trigger Period will be extended following consummation of a Change of Control for so long as either Rating Agency has publicly announced that it
is considering a possible ratings downgrade), and (ii)&nbsp;the notes of such series are rated below Investment Grade by both Rating Agencies on any day during the Trigger Period. </P>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">S-29 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Notwithstanding the foregoing, no Change of Control Triggering Event will be deemed to have
occurred in connection with any particular Change of Control unless and until such Change of Control has actually been consummated. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">&#147;Investment Grade&#148; means a rating of Baa3 or better by Moody&#146;s (or its equivalent under any successor rating category of
Moody&#146;s), a rating of BBB&#150; or better by S&amp;P (or its equivalent under any successor rating category of S&amp;P) and the equivalent investment grade credit rating from any replacement rating agency or rating agencies selected by us under
the circumstances permitting us to select a replacement agency and in the manner for selecting a replacement agency, in each case as set forth in the definition of &#147;Rating Agencies.&#148; </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">&#147;Moody&#146;s&#148; means Moody&#146;s Investors Service, Inc., and any successor to its rating agency business. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">&#147;Rating Agencies&#148; means Moody&#146;s and S&amp;P; <I>provided</I> that if any of Moody&#146;s or S&amp;P ceases to rate any series
of notes or fails to make a rating of any series of notes publicly available for reasons outside of the Company&#146;s control, the Company may appoint another &#147;nationally recognized statistical rating organization&#148; within the meaning of
Section&nbsp;3(a)(62) of the Exchange Act as a replacement for such Rating Agency with respect to such series of notes. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">&#147;S&amp;P&#148; means S&amp;P Global Ratings, a division of S&amp;P Global Inc., and any successor to its rating agency business. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">&#147;Voting Stock&#148; of any specified Person as of any date means the capital stock of such Person that is at the time entitled to vote
generally in the election of the board of directors of such Person. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The definition of &#147;Change of Control&#148; includes a phrase
relating to the direct or indirect sale, transfer, conveyance or other disposition of &#147;all or substantially all&#148; of the assets of the Company and its Subsidiaries taken as a whole. Although there is a limited body of case law interpreting
the phrase &#147;substantially all,&#148; there is no precise, established definition of the phrase under applicable law. Accordingly, the applicability of the requirement that the Company offers to purchase the notes of such series as a result of a
sale, transfer, conveyance or other disposition of less than all of the assets of the Company and its Subsidiaries taken as a whole to another &#147;person&#148; may be uncertain. In addition, holders of notes of any series may not be entitled to
require the Company to purchase their notes of such series in certain circumstances involving a significant change in the composition of the board of directors of the Company, including in connection with a proxy contest. Except as described above
with respect to a Change of Control, the indenture will not contain provisions that permit the holder of any notes of any series to require that we purchase or redeem the notes of such series in the event of a takeover, recapitalization or similar
transaction. </P> <P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B>Sinking Fund </B></P> <P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">There
will be no mandatory sinking fund payments for the notes. </P> <P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B>Book-entry System </B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Except as described in the accompanying prospectus under the heading &#147;Description of Debt Securities&#151;Registered Global
Securities,&#148; owners of beneficial interests in a Global Security will not be considered the holders thereof and will not be entitled to receive physical delivery of notes in definitive form, and no Global Security will be exchangeable except
for another Global Security of like denomination and terms to be registered in the name of the Depositary or its nominee. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The Depositary
has advised the Company that the Depositary is a limited-purpose trust company organized under the New York Banking Law, a &#147;banking organization&#148; within the meaning of New York Banking Law, a member of the Federal Reserve System, a
&#147;clearing corporation&#148; within the meaning of the New York Uniform Commercial Code, and a &#147;clearing agency&#148; registered pursuant to the provisions of Section&nbsp;17A of the Exchange Act. The Depositary was created to hold the
securities of its participants and to facilitate the clearance and </P>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">S-30 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman">
settlement of securities transactions among its participants in such securities through electronic book-entry changes in accounts of the participants, thereby eliminating the need for physical
movement of securities certificates. The Depositary&#146;s participants include securities brokers and dealers (including the underwriters), banks, trust companies, clearing corporations and certain other organizations some of whom (and/or their
representatives) own the Depositary. Access to the Depositary&#146;s book-entry system is also available to others, such as banks, brokers, dealers, trust companies and clearing corporations that clear through or maintain a custodial relationship
with a participant, either directly or indirectly. Persons who are not participants may beneficially own securities held by the Depositary only through participants. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">None of the Company, the Trustee or any paying agent will have any responsibility for the performance by the Depositary or its participants or
indirect participants of their respective obligations under the rules and procedures governing their operations. </P>
<P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B><FONT STYLE="white-space:nowrap">Same-day</FONT> Funds Settlement System and Payment </B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Settlement for the notes will be made by the underwriters in immediately available funds. All payments of principal and interest will be made
by the Company in immediately available funds. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The notes of each series will trade in the Depositary&#146;s <FONT
STYLE="white-space:nowrap">Same-Day</FONT> Funds Settlement System until maturity or earlier redemption, and secondary market trading activity in the notes of such series will therefore be required by the Depositary to settle in immediately
available funds. No assurance can be given as to the effect, if any, of settlement in immediately available funds on trading activity in the notes of such series. </P>
<P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B>Certain Covenants </B></P> <P STYLE="margin-top:6pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B><I>Limitation on Liens </I></B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Except as provided below, the Company shall not, and shall not permit any of its Restricted Subsidiaries to, directly or indirectly, create,
incur, issue, assume, guarantee or permit to exist any indebtedness for borrowed money (&#147;Indebtedness&#148;) secured by a Lien on any Principal Property or any shares of stock of or any Indebtedness of any Restricted Subsidiary, whether owned
on the date of issuance of the notes or thereafter acquired, unless the Company substantially contemporaneously secures the notes equally and ratably with (or prior to) such Indebtedness until such time as such Indebtedness is no longer secured by a
Lien on any Principal Property or any shares of stock of or any Indebtedness of any Restricted Subsidiary, except that the foregoing restrictions shall not apply to Indebtedness secured by: </P>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="5%" VALIGN="top" ALIGN="left">1.</TD>
<TD ALIGN="left" VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman; " ALIGN="left">Liens on any property, shares of stock or Indebtedness of any Person existing at the time such Person becomes a
Restricted Subsidiary; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="5%" VALIGN="top" ALIGN="left">2.</TD>
<TD ALIGN="left" VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman; " ALIGN="left">Liens on any property, shares of stock or Indebtedness existing at the time of acquisition of such property,
stock or Indebtedness by the Company or a Restricted Subsidiary; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="5%" VALIGN="top" ALIGN="left">3.</TD>
<TD ALIGN="left" VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman; " ALIGN="left">Liens to secure (i)&nbsp;the payment of all or any part of the price of acquisition, construction, alteration,
expansion, repair or improvement of property, assets or stock by the Company or a Restricted Subsidiary or (ii)&nbsp;any Indebtedness incurred by the Company or a Restricted Subsidiary prior to, at the time of or within one year after the later of
the acquisition or completion of construction, alteration, expansion, repair or improvement of such property (including any improvements on an existing property), which Indebtedness is incurred for the purpose of financing all or any part of the
purchase price thereof or construction, alteration, expansion, repair or improvements thereon; <I>provided</I>, <I>however</I>, that, in the case of any such acquisition, construction, alteration, expansion, repair or improvement, the Lien shall not
apply to any property theretofore owned by the Company or a Restricted Subsidiary, other than, in the case of any such construction, alteration, expansion, repair or improvement, any theretofore substantially unimproved real property on which the
property or improvement so constructed is located; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="5%" VALIGN="top" ALIGN="left">4.</TD>
<TD ALIGN="left" VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman; " ALIGN="left">Liens securing Indebtedness of the Company or a Restricted Subsidiary owing to the Company, a Restricted
Subsidiary or a wholly-owned Subsidiary; </P></TD></TR></TABLE>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">S-31 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">

<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="5%" VALIGN="top" ALIGN="left">5.</TD>
<TD ALIGN="left" VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman; " ALIGN="left">Liens on property of a Person existing at the time such Person is merged into or consolidated with the Company
or a Restricted Subsidiary or at the time of a sale, lease or other disposition of the properties of a Person as an entirety or substantially as an entirety to the Company or a Restricted Subsidiary; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="5%" VALIGN="top" ALIGN="left">6.</TD>
<TD ALIGN="left" VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman; " ALIGN="left">Liens on property of the Company or a Restricted Subsidiary in favor of the United States or any state thereof,
or any department, agency or instrumentality or political subdivision of the United States or any state thereof, or in favor of any other country or any political subdivision thereof, or any department, agency or instrumentality of such country or
political subdivision, to secure partial, progress, advance or other payments or performance pursuant to any contract or statute or to secure any Indebtedness incurred for the purpose of financing all or any part of the purchase price or the cost of
construction of the property subject to such Liens; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="5%" VALIGN="top" ALIGN="left">7.</TD>
<TD ALIGN="left" VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman; " ALIGN="left">Liens existing as of, or provided for under the terms of agreements existing as of, the date of the second
supplemental indenture, the third supplemental indenture or the fourth supplemental indenture, as applicable to such series of notes; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="5%" VALIGN="top" ALIGN="left">8.</TD>
<TD ALIGN="left" VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman; " ALIGN="left">Liens resulting from the deposit of funds or evidences of Indebtedness in trust for the purpose of defeasing
Indebtedness of the Company or any of its Restricted Subsidiaries; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="5%" VALIGN="top" ALIGN="left">9.</TD>
<TD ALIGN="left" VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman; " ALIGN="left">Liens to banks arising from the issuance of letters of credit issued by such banks (&#147;issuing banks&#148;)
which constitute borrowed money on the following: (i)&nbsp;any and all shipping documents, warehouse receipts, policies or certificates of insurance and other document accompanying or relative to drafts drawn under any credit, and any draft drawn
thereunder (whether or not such documents, goods or other property be released to or upon the order of the Company or any Subsidiary under a security agreement or trust or bailee receipt or otherwise), and the proceeds of each and all of the
foregoing; (ii)&nbsp;the balance of every deposit account, now or at the time hereafter existing, of the Company or any Subsidiary with the issuing banks, and any other claims of the Company or any Subsidiary against the issuing banks; and all
property claims and demands and all rights and interests therein of the Company or any Subsidiary and all evidences thereof and all proceeds thereof which have been or at any time will be delivered to or otherwise come into the issuing bank&#146;s
possession, custody or control, or into the possession, custody or control of any bailee for the issuing bank or of any of its agents or correspondents for the account of the issuing bank, for any purpose, whether or not the express purpose of being
used by the issuing bank as collateral security or for the safekeeping or for any other or different purpose, the issuing bank being deemed to have possession or control of all of such property actually in transit to or from or set apart for the
issuing bank, any bailee for the issuing bank or any of its correspondents for other acting in its behalf, it being understood that the receipt at any time by the issuing bank, or any of its bailees, agents or correspondents, or other security, of
whatever nature, including cash, will not be deemed a waiver of any of the issuing bank&#146;s rights or power hereunder; (iii)&nbsp;all property shipped under or pursuant to or in connection with any credit or drafts drawn thereunder or in any way
related thereto, and all proceeds thereof; or (iv)&nbsp;all additions to and substitutions for any of the property enumerated above in this subsection; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="5%" VALIGN="top" ALIGN="left">10.</TD>
<TD ALIGN="left" VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman; " ALIGN="left">Any extension, renewal or replacement (or successive extensions, renewals or replacements) in whole or in part
of any Liens referred to in clauses (1)&nbsp;through (9) above; <I>provided</I>, <I>however</I>, that the principal amount of Indebtedness so secured shall not exceed the principal amount of Indebtedness so secured at the time of such extension,
renewal or replacement or, if greater, the committed amount of Indebtedness originally secured by such Liens (plus, in each case, the aggregate amount of premiums, other payments, costs and expenses related to any refinancing, refunding, extension,
renewal or replacement of such Indebtedness), and that such extension, renewal or replacement shall be limited to all or a part of the property which secured the Liens so extended, renewed or replaced (<I>plus</I> improvements and construction on
such property); </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="5%" VALIGN="top" ALIGN="left">11.</TD>
<TD ALIGN="left" VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman; " ALIGN="left">Liens securing the payment of taxes, special assessments, governmental charges or claims which are not overdue
for a period of more than sixty days or the validity of which is being contested by the </P></TD></TR></TABLE>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">S-32 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">

<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="9%">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top">
Person being charged in good faith by appropriate proceedings, and as to which it has set aside on its books adequate reserves to the extent required by GAAP; </TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="5%" VALIGN="top" ALIGN="left">12.</TD>
<TD ALIGN="left" VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman; " ALIGN="left">deposits, pledges or Liens on or securing property or shares of stock under workers&#146; compensation,
unemployment insurance and social security laws or similar obligations, or to secure the performance of bids, tenders, contracts (other than for the repayment of borrowed money), leases, bankers&#146; acceptances or completion guarantees, or to
secure statutory or regulatory obligations or surety or appeal bonds and related indemnification obligations in respect thereof, government contracts, performance and
<FONT STYLE="white-space:nowrap"><FONT STYLE="white-space:nowrap">return-of-money</FONT></FONT> bonds and other obligations of a similar nature, or to secure indemnity, performance or other similar bonds in the ordinary course of business;
</P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="5%" VALIGN="top" ALIGN="left">13.</TD>
<TD ALIGN="left" VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman; " ALIGN="left">any attachment Lien being contested in good faith and by proceedings promptly initiated and diligently
conducted, unless the attachment giving rise thereto will not, within sixty days after the entry thereof, have been discharged or fully bonded or will not have been discharged within sixty days after the termination of any such bond;
</P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="5%" VALIGN="top" ALIGN="left">14.</TD>
<TD ALIGN="left" VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman; " ALIGN="left">any judgment Lien or Lien securing or arising from the rendering of a decree, attachment, award or order unless
(i)&nbsp;the judgment it secures will not, within sixty days after the entry thereof, have been discharged or execution thereof stayed pending appeal, or will not have been discharged within sixty days after the expiration of any such stay or
(ii)&nbsp;the judgment it secures results in an Event of Default; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="5%" VALIGN="top" ALIGN="left">15.</TD>
<TD ALIGN="left" VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman; " ALIGN="left">easements, <FONT STYLE="white-space:nowrap"><FONT STYLE="white-space:nowrap">rights-of-way,</FONT></FONT>
zoning restrictions, servitudes, encroachments, title defects or other irregularities, and servicing agreements, development agreements, site plan agreements, subdivision agreements, facilities sharing agreements, cost sharing agreements and other
agreements, and other restrictions, charges or encumbrances not materially interfering with the ordinary conduct of the business; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="5%" VALIGN="top" ALIGN="left">16.</TD>
<TD ALIGN="left" VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman; " ALIGN="left">any statutory or governmental Lien or a Lien arising by operation of law, or any mechanics&#146;,
repairmen&#146;s, materialmen&#146;s, supplier&#146;s, carrier&#146;s, landlord&#146;s, warehousemen&#146;s, construction contractor&#146;s or similar Lien or pursuant to customary reservations or retentions of title in each case for sums not yet
overdue for a period of more than sixty days or that are bonded or being contested in good faith by appropriate proceedings and any undetermined Lien that is incidental to construction, development, improvement or repair; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="5%" VALIGN="top" ALIGN="left">17.</TD>
<TD ALIGN="left" VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman; " ALIGN="left">leases or subleases granted to others that do not materially interfere with the ordinary course of business of
the Company and its Subsidiaries, taken as a whole, and any Lien of a lessor in the property subject to any operating lease or short-term rental; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="5%" VALIGN="top" ALIGN="left">18.</TD>
<TD ALIGN="left" VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman; " ALIGN="left">Liens encumbering property or assets under construction or arising from progress or partial payments by a third
party relating to such property or assets; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="5%" VALIGN="top" ALIGN="left">19.</TD>
<TD ALIGN="left" VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman; " ALIGN="left">Liens arising from filing Uniform Commercial Code financing statements (or equivalent filings, registrations or
agreements in foreign jurisdictions) regarding operating leases or short-term rentals; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="5%" VALIGN="top" ALIGN="left">20.</TD>
<TD ALIGN="left" VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman; " ALIGN="left">Liens encumbering customary initial deposits and margin deposits, and other Liens that are within the general
parameters customary in the industry and incurred in the ordinary course of business, in each case, securing Indebtedness under interest rate agreements, currency agreements or commodity agreements designed to protect the Company or any of its
Subsidiaries from fluctuations in interest rates, currencies or the price of commodities; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="5%" VALIGN="top" ALIGN="left">21.</TD>
<TD ALIGN="left" VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman; " ALIGN="left">Liens on or sales of receivables; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="5%" VALIGN="top" ALIGN="left">22.</TD>
<TD ALIGN="left" VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman; " ALIGN="left">Liens in favor of governmental bodies to secure advance or progress payments pursuant to any contract or
statute and Liens in favor of governmental bodies in connection with industrial revenue, pollution control, private activity bonds or similar financing; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="5%" VALIGN="top" ALIGN="left">23.</TD>
<TD ALIGN="left" VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman; " ALIGN="left">restrictions on dispositions of property, assets or stock to be disposed of pursuant to merger agreements,
stock or asset purchase agreements and similar agreements, Liens on cash earnest money deposits made in connection with any letter of intent or purchase agreement and customary options, put
</P></TD></TR></TABLE>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">S-33 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">

<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="9%">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top">
and call arrangements, rights of first refusal and similar rights relating to investments in joint ventures and partnerships; </TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="5%" VALIGN="top" ALIGN="left">24.</TD>
<TD ALIGN="left" VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman; " ALIGN="left">Liens of sellers of goods arising under Article 2 of the Uniform Commercial Code or similar provisions of
applicable law in the ordinary course of business, covering only the goods sold and securing only the unpaid purchase price for such goods and related expenses; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="5%" VALIGN="top" ALIGN="left">25.</TD>
<TD ALIGN="left" VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman; " ALIGN="left">Liens on machinery and equipment in favor of contract counterparties arising under contracts entered into in
the ordinary course of business, provided that such Liens secure only future performance; or </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="4%">&nbsp;</TD>
<TD WIDTH="5%" VALIGN="top" ALIGN="left">26.</TD>
<TD ALIGN="left" VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman; " ALIGN="left">any Lien securing Indebtedness of a Person which is a Successor Company (as defined below) to the Company to
the extent permitted under &#147;&#151;Consolidation, Merger and Sale of Assets.&#148; </P></TD></TR></TABLE> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Notwithstanding the foregoing,
the Company and its Restricted Subsidiaries may, without securing the notes, create, incur, issue, assume, guarantee or permit to exist any Indebtedness secured by a Lien, other than those permitted pursuant to clauses (1)&nbsp;through (26) above,
if, immediately after giving pro forma effect to the Incurrence of such Indebtedness (and the receipt and application of the proceeds thereof) or the securing of outstanding Indebtedness, the sum of (without duplication)&nbsp;(i) all Indebtedness of
the Company and its Restricted Subsidiaries secured by Liens (other than those Liens permitted pursuant to clauses (1)&nbsp;through (26) above) and (ii)&nbsp;all Attributable Indebtedness in respect of Sale/Leaseback Transactions with respect to any
Principal Property, at the time of determination, does not exceed 15% of Consolidated Net Tangible Assets. </P> <P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B><I>Limitation on Sale/Leaseback
Transactions </I></B></P> <P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The Company shall not, and shall not permit any of its Restricted Subsidiaries to, enter into any Sale/Leaseback
Transaction with respect to any Principal Property, unless (i)&nbsp;the Company or such Restricted Subsidiary would be entitled to create a Lien on such Principal Property securing Indebtedness in an amount equal to the Attributable Indebtedness
with respect to such Sale/Leaseback Transaction without securing the notes pursuant to the covenant described in &#147;Limitation on Liens&#148; above or (ii)&nbsp;the Company, within twelve months from the effective date of such Sale/Leaseback
Transaction, applies to (x)&nbsp;the voluntary defeasance or retirement (excluding retirements of notes and other Indebtedness ranking pari passu with the notes as a result of conversions, pursuant to mandatory sinking funds or mandatory prepayment
provisions or by payment at maturity) of notes or other Indebtedness ranking pari passu with the notes, (y)&nbsp;the acquisition, construction, development or improvement of any Principal Property used or useful in the businesses of the Company or
its Subsidiaries or (z)&nbsp;any combination of the foregoing, an amount equal to the Attributable Indebtedness with respect to such Sale/Leaseback Transaction. </P>
<P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B><I>Consolidation, Merger and Sale of Assets </I></B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The Company may not consolidate with or merge with or into any person, or convey, transfer or lease all or substantially all of its assets,
unless the following conditions have been satisfied: </P> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">either (1)&nbsp;the Company is the continuing person in the case of a merger or (2)&nbsp;the resulting, surviving
or transferee person, if other than the Company (the &#147;Successor Company&#148;), is a corporation organized and existing under the laws of the United States, any State thereof or the District of Columbia and expressly assumes pursuant to a
supplemental indenture all of the obligations of the Company under the notes and the indenture; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">immediately after giving effect to such transaction (and treating any indebtedness that becomes an obligation of
the Successor Company or any subsidiary of the Company as a result of such transaction as having been incurred by the Successor Company or such subsidiary at the time of such transaction), no default or Event of Default would occur or be continuing;
and </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the Company has delivered to the Trustee an officers&#146; certificate and an opinion of counsel (which opinion
of counsel may be subject to customary assumptions, qualifications and exclusions), each stating that such consolidation, merger, or transfer and such supplemental indenture (if any) comply with the indenture. </P></TD></TR></TABLE>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">S-34 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">If the Successor Company expressly assumes all of the obligations of the Company under the
notes and the indenture, the Company will promptly thereafter be released from such obligations. </P> <P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B><I>Reports </I></B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The indenture provides that so long as any notes of the applicable series are outstanding, if the Company is subject to the periodic reporting
requirements of the Exchange Act, it will furnish to the Trustee and the holders (unless such reports are available on the SEC&#146;s Electronic Data Gathering, Analysis and Retrieval (EDGAR) system or any successor thereto) copies of the annual
reports and of the information, documents and other reports the Company is required to file with the SEC pursuant to Section&nbsp;13 or Section&nbsp;15(d) of the Exchange Act within 15 days after the Company is required to file such reports with the
SEC. If the Company is not subject to the periodic reporting requirements of the Exchange Act, then the Company will file with the Trustee and the holders (unless such reports are available on the EDGAR system or any successor thereto) and the SEC,
in accordance with the SEC&#146;s rules and regulations, such of the supplementary and periodic information, documents and reports which may be required pursuant to Section&nbsp;13 of the Exchange Act in respect of a security listed and registered
on a national securities exchange as may be prescribed from time to time in such rules and regulations. Delivery of such statements, reports, notices and other information and documents to the Trustee is for informational purposes only and the
Trustee&#146;s receipt of the foregoing shall not constitute constructive notice of any information contained therein or determinable from information contained therein, including the Company&#146;s compliance with any of the covenants in the
indenture (as to which the Trustee is entitled to rely exclusively on officers&#146; certificates and other certificates pursuant to the terms of the indenture). </P>
<P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B><I>Certain Definitions </I></B></P> <P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The following
definitions, among others, are used in the indenture. Many of the definitions of terms used in the indenture have been negotiated specifically for the purposes of inclusion in the indenture and may not be consistent with the manner in which such
terms are defined in other contexts. Prospective purchasers of notes are encouraged to read each of the following definitions carefully and to consider such definitions in the context in which they are used in the indenture. Capitalized terms used
herein but not defined have the meanings assigned thereto in the indenture. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">&#147;<I>Attributable Indebtedness</I>&#148; with respect to
a Sale/Leaseback Transaction means, as of the time of determination, (i)&nbsp;if the obligation with respect to such Sale/Leaseback Transaction is a Finance Lease Obligation, the amount of such obligation determined in accordance with GAAP and
included in the financial statements of the lessee or (ii)&nbsp;if the obligation with respect to such Sale/Leaseback Transaction is not a Finance Lease Obligation, the total Net Amount of Rent required to be paid by the lessee under such lease
during the remaining term thereof (including any period for which the lease has been extended), discounted from the respective due dates thereof to such determination date at the rate per annum borne by the applicable notes compounded semi-annually.
</P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">&#147;<I>Captive Insurance Subsidiary</I>&#148; means any Subsidiary of the Company that is subject to regulation as an insurance company
(or any Subsidiary thereof). </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">&#147;<I>Consolidated Net Tangible Assets</I>&#148; means, as of any date of determination, the sum of the
amounts that would appear on a consolidated balance sheet of the Company and its Subsidiaries for the total assets (less accumulated depletion, depreciation and amortization, allowances for doubtful receivables, other applicable reserves and other
properly deductible items) of the Company and its Subsidiaries, determined on a consolidated basis in accordance with GAAP, after giving effect to purchase accounting and after deducting therefrom, to the extent included in total assets, in each
case as determined on a consolidated basis in accordance with GAAP (without duplication): (i) the aggregate amount of liabilities of the Company and its Subsidiaries that may properly be classified as current liabilities (including taxes accrued as
estimated) (excluding the amount of those which are by their terms extendable or renewable at the option of the obligor to a date more than twelve months after the date as of which the amount is being determined); (ii) current Indebtedness and
current maturities of </P>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">S-35 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman">
long-term Indebtedness; (iii)&nbsp;minority interests in the Company&#146;s Subsidiaries held by Persons other than the Company or a wholly-owned Subsidiary of the Company; and
(iv)&nbsp;unamortized debt discount and expenses and other unamortized deferred charges, goodwill, patents, trademarks, service marks, trade names, copyrights, licenses, organization or developmental expenses and other intangible items. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">&#147;<I>Finance Lease Obligation</I>&#148; means an obligation that is required to be accounted for as a finance lease (and, for the
avoidance of doubt, not an operating lease) on both the balance sheet and income statement for financial reporting purposes in accordance with GAAP. At the time any determination thereof is to be made, the amount of the liability in respect of a
finance lease would be the amount required to be reflected as a liability on such balance sheet (excluding the footnotes thereto) in accordance with GAAP. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">&#147;<I>Fund Entity</I>&#148; means any Subsidiary of the Company, 100% of whose capital stock is at the time owned by the Company directly
or indirectly through other Persons 100% of whose capital stock is at the time owned, directly or indirectly, by the Company (other than, in the case of any Subsidiary that is not organized or existing under the laws of the United States, any state
of the United States or the District of Columbia, with respect to any directors&#146; qualifying shares), which does not act other than either (a)&nbsp;solely as the general partner of one or more of the Company&#146;s Investment Funds or
(b)&nbsp;solely for the purpose of being a registered investment adviser for any of such Investment Funds, whether directly or indirectly through the general partner of such Investment Fund. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">&#147;<I>GAAP</I>&#148; means generally accepted accounting principles in the United States as in effect as of the date on which the notes are
issued, including those set forth in the opinions and pronouncements of the Accounting Principles Board of the American Institute of Certified Public Accountants and statements and pronouncements of the Financial Accounting Standards Board or in
such other statements by such other entity as approved by a significant segment of the accounting profession. All ratios and computations based on GAAP contained in the indenture will be computed in conformity with GAAP consistently applied. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">&#147;<I>Investment Fund</I>&#148; means any foreign or domestic limited partnership, limited liability company or other investment vehicle
with respect to which a Fund Entity acts as a general partner and/or its registered investment adviser, whether directly or indirectly through the general partner of such Investment Fund, and in which the Company and/or one or more of its
Subsidiaries holds no more than a minority equity interest. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">&#147;<I>Lien</I>&#148; means any mortgage, pledge, security interest,
encumbrance, lien or charge of any kind (including any conditional sale or other title retention agreement or lease in the nature thereof). </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">&#147;<I>Net Amount of Rent</I>&#148; as to any lease for any period means the aggregate amount of rent payable by the lessee with respect to
such period after excluding amounts required to be paid on account of maintenance and repairs, insurance, taxes, assessments, water rates and similar charges. In the case of any lease that is terminable by the lessee upon the payment of a penalty,
such net amount shall also include the amount of such penalty, but no rent shall be considered as payable under such lease subsequent to the first date upon which it may be so terminated. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">&#147;<I>Person</I>&#148; means any individual, corporation, partnership, limited liability company, joint venture, association, joint-stock
company, trust, unincorporated organization, government or any agency or political subdivision thereof or any other entity. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">&#147;<I>Principal Property</I>&#148; means any manufacturing plant or other similar facility (including Production Machinery and Equipment
located thereon), corporate office, equipment yard, maintenance facility, training facility or warehouse owned by the Company or any Subsidiary, which is located within the United States (excluding its territories and possessions), in each case
having a net book value in excess of 1% of Consolidated Net Tangible Assets other than (i)&nbsp;any such plant, facility or property which the Company&#146;s Board of Directors determines in good faith is not of material importance to the total
business conducted, or assets owned, by the Company and its Subsidiaries as an entirety or (ii)&nbsp;any portion of any such plant, facility or property which the Company&#146;s Board of Directors determines in good faith not to be of material
importance to the use or operation thereof. </P>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">S-36 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">&#147;<I>Production Machinery and Equipment</I>&#148; means production machinery and
equipment in such Principal Property used directly in the production of the Company&#146;s or any Subsidiary&#146;s products. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">&#147;<I>Restricted Subsidiary</I>&#148; means any Subsidiary of the Company (other than any Fund Entity or Captive Insurance Subsidiary),
substantially all of the assets of which are located in the United States (excluding its territories and possessions) that at the time, directly or indirectly, through one or more Subsidiaries or in combination with one or more other Subsidiaries or
the Company, owns a Principal Property; provided, however, that any Subsidiary that transacts any substantial portion of its business and regularly maintains any substantial portion of its fixed assets outside of the United States (excluding its
territories and possessions) shall not be deemed to be a &#147;Restricted Subsidiary.&#148; </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">&#147;<I>Sale/Leaseback Transaction</I>&#148;
means an arrangement relating to property owned on the date of issuance of the notes or thereafter acquired whereby the Company or any of its Restricted Subsidiaries transfers such property to a Person and the Company or any of its Restricted
Subsidiaries leases it from such Person other than (1)&nbsp;leases for a term, including renewals at the option of the lessee, of not more than five years, (2)&nbsp;leases between the Company and a Subsidiary or between Subsidiaries and
(3)&nbsp;leases of a property executed by the time of, or within twelve months after the latest of, the acquisition, the completion of construction or improvement, or the commencement of commercial operation of such property. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">&#147;<I>Subsidiary</I>&#148; of any Person means any corporation, association, partnership or other business entity of which more than 50% of
the total voting power of shares of Capital Stock entitled (without regard to the occurrence of any contingency) to vote in the election of directors, managers or trustees thereof is at the time owned or controlled, directly or indirectly, by
(i)&nbsp;such Person, (ii)&nbsp;such Person and one or more Subsidiaries of such Person or (iii)&nbsp;one or more Subsidiaries of such Person; provided, however, that any Person the accounts of which are not consolidated with those of the Company in
its consolidated financial statements prepared in accordance with GAAP shall not be deemed to be a &#147;Subsidiary&#148; of the Company. </P> <P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B>Events of
Default and Remedies </B></P> <P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The following will constitute &#147;Events of Default&#148; under the indenture with respect to the notes of each
series, subject to any additional limitations and qualifications included in the indenture: </P> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="9%">&nbsp;</TD>
<TD WIDTH="4%" VALIGN="top" ALIGN="left">(1)</TD>
<TD ALIGN="left" VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman; " ALIGN="left">default in the payment of any installment of interest on the notes of such series as and when the same become
due and payable and continuance of such default for a period of 30 days; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="9%">&nbsp;</TD>
<TD WIDTH="4%" VALIGN="top" ALIGN="left">(2)</TD>
<TD ALIGN="left" VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman; " ALIGN="left">default in the payment of principal or premium, if any, with respect to the notes of such series as and when
the same become due and payable, whether at maturity, upon redemption, by declaration, upon required purchase or otherwise; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="9%">&nbsp;</TD>
<TD WIDTH="4%" VALIGN="top" ALIGN="left">(3)</TD>
<TD ALIGN="left" VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman; " ALIGN="left">default in the payment of any sinking fund payment with respect to the notes of such series as and when the
same become due and payable and continuance of such default for a period of 30&nbsp;days; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="9%">&nbsp;</TD>
<TD WIDTH="4%" VALIGN="top" ALIGN="left">(4)</TD>
<TD ALIGN="left" VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman; " ALIGN="left">failure on the part of the Company to comply with any of the covenants or agreements on the part of the Company
in the notes of such series, in any resolution of the Board of Directors of the Company authorizing the issuance of the notes of such series, in the indenture for the benefit of such series of notes or in any supplemental indenture with respect to
the notes of such series (other than a covenant a default in the performance of which is otherwise specifically dealt with) continuing for a period of 90 days after the date on which written notice specifying such failure and requiring the Company
to remedy the same has been given, by registered or certified mail or by overnight courier guaranteeing next day delivery, to the Company by the Trustee or to the Company and the Trustee by the holders of at least 25% in aggregate principal amount
of the notes of such series at the time outstanding; </P></TD></TR></TABLE>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">S-37 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">

<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="9%">&nbsp;</TD>
<TD WIDTH="4%" VALIGN="top" ALIGN="left">(5)</TD>
<TD ALIGN="left" VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman; " ALIGN="left">indebtedness for money borrowed of the Company or any Restricted Subsidiary of the Company is not paid within
any applicable grace period after final maturity or is accelerated prior to its stated final maturity by the holders thereof because of a default, the total principal amount of such indebtedness unpaid or accelerated exceeds $150.0&nbsp;million or
the United States dollar equivalent thereof at the time and such default remains uncured or such acceleration is not rescinded or annulled for 30 days after the date on which written notice specifying such failure and requiring the Company to remedy
the same has been given, by registered or certified mail or by overnight courier guaranteeing next day delivery, to the Company by the Trustee or to the Company and the Trustee by the holders of at least 25% in aggregate principal amount of the
notes of such series at the time outstanding; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="9%">&nbsp;</TD>
<TD WIDTH="4%" VALIGN="top" ALIGN="left">(6)</TD>
<TD ALIGN="left" VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman; " ALIGN="left">the Company or any of its Restricted Subsidiaries (1)&nbsp;voluntarily commences any proceeding or files any
petition seeking relief under the United States Bankruptcy Code or other federal or state bankruptcy, insolvency or similar law, (2)&nbsp;consents to the institution of, or fails to controvert within the time and in the manner prescribed by law, any
such proceeding or the filing of any such petition, (3)&nbsp;applies for or consents to the appointment of a receiver, trustee, custodian, sequestrator or similar official for the Company or any such Restricted Subsidiary or for a substantial part
of its property, (4)&nbsp;files an answer admitting the material allegations of a petition filed against it in any such proceeding, (5)&nbsp;makes a general assignment for the benefit of creditors, (6)&nbsp;admits in writing its inability to pay, or
fails generally to pay, its debts as they become due or (7)&nbsp;takes any comparable action under any foreign laws relating to insolvency; and </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="9%">&nbsp;</TD>
<TD WIDTH="4%" VALIGN="top" ALIGN="left">(7)</TD>
<TD ALIGN="left" VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman; " ALIGN="left">the entry of an order or decree by a court having competent jurisdiction for (1)&nbsp;relief with respect to
the Company or any of its Restricted Subsidiaries or a substantial part of any of their property under the United States Bankruptcy Code or any other federal or state bankruptcy, insolvency or similar law, (2)&nbsp;the appointment of a receiver,
trustee, custodian, sequestrator or similar official for the Company or any such Restricted Subsidiary or for a substantial part of any of their property (except any decree or order appointing such official of such Restricted Subsidiary pursuant to
a plan under which the assets and operations of such Restricted Subsidiary are transferred to or combined with another one or more other Restricted Subsidiaries or Subsidiaries or to or with the Company) or (3)&nbsp;the <FONT
STYLE="white-space:nowrap">winding-up</FONT> or liquidation of the Company or any such Restricted Subsidiary (except any decree or order approving or ordering the <FONT STYLE="white-space:nowrap">winding-up</FONT> or liquidation of the affairs of a
Restricted Subsidiary pursuant to a plan under which the assets and operations of such Restricted Subsidiary are transferred to or combined with one or more other Restricted Subsidiaries or Subsidiaries or to or with the Company), and such order or
decree continues unstayed and in effect for 90 consecutive days, or any similar relief is granted under any foreign laws and the order or decree stays in effect for 90 consecutive days. </P></TD></TR></TABLE>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">If an Event of Default described in the first, second, third, fourth or fifth clauses above occurs and is continuing with respect to the notes
of such series, unless the principal and interest with respect to all the notes of such series has already become due and payable, either the Trustee or the holders of not less than 25% in aggregate principal amount of the notes of such series then
outstanding may declare the principal of and interest on all the notes of such series due and payable immediately. If an Event of Default described in the sixth or seventh clauses above occurs, unless the principal and interest with respect to all
the notes of such series has become due and payable, the principal of and interest on all the notes of such series will become and be immediately due and payable without any declaration or other act on the part of the Trustee or any holder of notes
of such series. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">If an Event of Default occurs and is continuing, the Trustee will be entitled and empowered to institute any action or
proceeding for the collection of the sums so due and unpaid or to enforce the performance of any provision of the notes of such series or the indenture for the benefit of such series of notes, to prosecute any such action or proceeding to judgment
or final decree and to enforce any such judgment or final decree against the Company or any other obligor on the notes of such series. In addition, if there are any pending proceedings for </P>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">S-38 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman">
the bankruptcy or reorganization of the Company or any other obligor on the notes of such series, or if a receiver, trustee or similar official has been appointed for its property, the Trustee
will be entitled and empowered to file and prove a claim for the whole amount of principal, premium, if any, and interest owing and unpaid with respect to the notes of such series. No holder of any notes of such series will have any right to
institute any action or proceeding upon, under or with respect to the indenture, for the appointment of a receiver or trustee or for any other remedy, unless (1)&nbsp;such holder previously has given to the Trustee written notice of an Event of
Default with respect to the notes of such series and of the continuance thereof, (2)&nbsp;the holders of not less than 25% in aggregate principal amount of the outstanding notes of such series have made written request to the Trustee to institute
such action or proceeding with respect to such Event of Default and have offered to the Trustee such security or indemnity as it may require against the costs, expenses, and liabilities to be incurred therein or thereby and (3)&nbsp;the Trustee, for
60 days after its receipt of such notice, request and offer of security or indemnity, has failed to institute such action or proceeding and no direction inconsistent with such written request has been given to the Trustee pursuant to the provisions
of the indenture. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Prior to the acceleration of the maturity of the notes of such series, the holders of a majority in aggregate principal
amount of the notes of such series at the time outstanding may, on behalf of the holders of all the notes of such series, waive any past default or Event of Default and its consequences for the notes of such series, except (1)&nbsp;a default in the
payment of the principal, premium, if any, or interest with respect to such notes or (2)&nbsp;a default with respect to a provision of the indenture that cannot be amended without the consent of each holder affected thereby. In the case of any such
waiver, such default will cease to exist, any Event of Default arising therefrom will be deemed to have been cured for all purposes and the Company, the Trustee and the holders of the notes of such series will be restored to their former positions
and rights under the indenture. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The Trustee is required to give, within 90 days after the occurrence of a default actually known to a
responsible officer of the Trustee with respect to the notes of each series, to the holders of the notes of such series notice of all defaults with respect to the notes of such series so known to it, unless such defaults have been cured or waived
before the giving of such notice; provided, however, that except in the case of default in the payment of principal, premium, if any, or interest with respect to the notes of such series or in the making of any sinking fund or purchase fund payment
with respect to the notes of such series, the Trustee will be protected in withholding such notice if it in good faith determines that the withholding of such notice is in the interest of the holders of such notes. </P>
<P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B>Defeasance; Satisfaction and Discharge </B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The notes of each series will be subject to defeasance and discharge, and the covenants set forth above under &#147;&#151;Certain
Covenants&#151;Limitation on Liens&#148; and &#147;&#151;Certain Covenants&#151;Limitation on Sale/Leaseback Transactions&#148; and &#147;&#151;Certain Covenants&#151;Consolidation, Merger and Sale of Assets&#148; and &#147;&#151;Certain
Covenants&#151;Reports&#148; will be subject to covenant defeasance, as set forth in the indenture. See &#147;Description of Debt Securities&#151;Satisfaction and Discharge of the Indenture; Defeasance&#148; in the accompanying prospectus. </P>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">S-39 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center"><B><A NAME="supprom326517_9"></A>MATERIAL U.S. FEDERAL INCOME TAX CONSEQUENCES </B></P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The following discussion is a summary of the material U.S. federal income tax consequences of the purchase, ownership and disposition of the
notes issued pursuant to this offering, but does not purport to be a complete analysis of all potential U.S. federal income tax effects. The effects of other U.S. federal tax laws, such as estate and gift tax laws, and any applicable state, local or
foreign tax laws are not discussed. This discussion is based on the U.S. Internal Revenue Code of 1986, as amended (the &#147;Code&#148;), Treasury Regulations promulgated thereunder, judicial decisions, and published rulings and administrative
pronouncements of the U.S. Internal Revenue Service (the &#147;IRS&#148;), in each case in effect as of the date hereof. These authorities may change or be subject to differing interpretations. Any such change or differing interpretation may be
applied retroactively in a manner that could adversely affect a holder of the notes. We have not sought and will not seek any rulings from the IRS regarding the matters discussed below. There can be no assurance that the IRS or a court will not take
a position contrary to that discussed below regarding the U.S. federal income tax consequences of the purchase, ownership and disposition of the notes. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">This discussion is limited to the notes that are held as &#147;capital assets&#148; within the meaning of Section&nbsp;1221 of the Code
(generally, property held for investment). In addition, this discussion is limited to the notes that are purchased for cash at original issue and at the original &#147;issue price&#148; of the applicable series of the notes within the meaning of
Section&nbsp;1273 of the Code (<I>i.e.</I>, the first price at which a substantial amount of the applicable series of notes is sold to investors for cash, excluding sales to bond houses, brokers or similar persons or organizations acting in the
capacity of underwriters, placement agents or wholesalers). This discussion does not address all U.S. federal income tax consequences relevant to a holder&#146;s particular circumstances, including the impact of the Medicare contribution tax on net
investment income or the alternative minimum tax. In addition, it does not address consequences relevant to holders subject to special rules, including, without limitation: </P> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="1%">&nbsp;</TD>
<TD WIDTH="2%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">U.S. expatriates and former citizens or long-term residents of the United States; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="1%">&nbsp;</TD>
<TD WIDTH="2%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">U.S. Holders (as defined below) whose functional currency is not the U.S. dollar; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="1%">&nbsp;</TD>
<TD WIDTH="2%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">U.S. Holders (as defined below) who hold notes through <FONT STYLE="white-space:nowrap">non-U.S.</FONT> brokers
or other <FONT STYLE="white-space:nowrap">non-U.S.</FONT> intermediaries; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="1%">&nbsp;</TD>
<TD WIDTH="2%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">persons holding the notes as part of a hedge, straddle or other risk reduction strategy or as part of a
conversion transaction or other integrated investment; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="1%">&nbsp;</TD>
<TD WIDTH="2%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">banks, insurance companies, and other financial institutions; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="1%">&nbsp;</TD>
<TD WIDTH="2%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">real estate investment trusts or regulated investment companies; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="1%">&nbsp;</TD>
<TD WIDTH="2%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">brokers, dealers or traders in securities; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="1%">&nbsp;</TD>
<TD WIDTH="2%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">&#147;controlled foreign corporations,&#148; &#147;passive foreign investment companies,&#148; and corporations
that accumulate earnings to avoid U.S. federal income tax; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="1%">&nbsp;</TD>
<TD WIDTH="2%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">entities or arrangements treated as partnerships or S corporations for U.S. federal income tax purposes (and
investors therein); </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="1%">&nbsp;</TD>
<TD WIDTH="2%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt"><FONT STYLE="white-space:nowrap">tax-exempt</FONT> entities or governmental entities; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="1%">&nbsp;</TD>
<TD WIDTH="2%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">persons deemed to sell the notes under the constructive sale provisions of the Code; and </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="1%">&nbsp;</TD>
<TD WIDTH="2%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">persons subject to special tax accounting rules as a result of any item of gross income with respect to the notes
being taken into account in an applicable financial statement. </P></TD></TR></TABLE> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">If an entity or other arrangement treated as a
partnership for U.S. federal income tax purposes holds notes, the tax treatment of a partner in the partnership will depend on the status of the partner, the activities of the partnership and certain determinations made at the partner level.
Accordingly, partnerships considering an investment in the notes and partners in such partnerships should consult their tax advisors regarding the U.S. federal income tax consequences to them. </P>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">S-40 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B>THIS DISCUSSION IS FOR INFORMATIONAL PURPOSES ONLY AND IS NOT TAX ADVICE. PROSPECTIVE INVESTORS SHOULD
CONSULT THEIR TAX ADVISORS WITH RESPECT TO THE APPLICATION OF THE U.S. FEDERAL INCOME TAX LAWS TO THEIR PARTICULAR SITUATIONS AS WELL AS ANY TAX CONSEQUENCES OF THE PURCHASE, OWNERSHIP AND DISPOSITION OF THE NOTES ARISING UNDER OTHER U.S. FEDERAL
TAX LAWS (INCLUDING ESTATE AND GIFT TAX LAWS), UNDER THE LAWS OF ANY STATE, LOCAL OR <FONT STYLE="white-space:nowrap">NON-U.S.</FONT> TAXING JURISDICTION OR UNDER ANY APPLICABLE TAX TREATY. </B></P>
<P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B>Effects of Certain Contingencies </B></P> <P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">We may
pay amounts in excess of the stated interest and principal payable on the notes or make payments in advance of their scheduled times, as described above under &#147;Description of Notes&#151;Purchase upon a Change of Control Triggering Event,&#148;
&#147;Description of Notes&#151;Optional Redemption&#148; and &#147;Description of Notes&#151;Special Mandatory Redemption.&#148; These contingencies may implicate the provisions of the Treasury Regulations governing &#147;contingent payment debt
instruments,&#148; which could cause the timing, amount and character of a holder&#146;s income, gain or loss with respect to the notes to be different from the consequences discussed herein. We believe and intend to take the position, and the
remainder of this discussion assumes, that the notes are not contingent payment debt instruments within the meaning of the applicable Treasury Regulations. Our position is binding on a holder unless such holder discloses a contrary position in the
manner that is required by the applicable Treasury Regulations. Our position is not, however, binding on the IRS. It is possible that the IRS might take a different position from that described above. In that case, if such position is sustained, a
holder might be required to accrue interest income at a higher rate than the stated interest rate and to treat as ordinary income rather than capital gain part or all of the gain recognized on the taxable disposition of the notes. Holders should
consult their tax advisors regarding the possible application of the contingent payment debt instrument rules to the notes. </P> <P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B>Tax Consequences
Applicable to U.S. Holders </B></P> <P STYLE="margin-top:6pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B><I>Definition of a U.S. Holder </I></B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">For purposes of this discussion, a &#147;U.S. Holder&#148; is a beneficial owner of a note that, for U.S. federal income tax purposes, is or is
treated as: </P> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="1%">&nbsp;</TD>
<TD WIDTH="2%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">an individual who is a citizen or resident of the United States; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="1%">&nbsp;</TD>
<TD WIDTH="2%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">a corporation created or organized under the laws of the United States, any state thereof or the District of
Columbia; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="1%">&nbsp;</TD>
<TD WIDTH="2%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">an estate, the income of which is subject to U.S. federal income tax regardless of its source; or
</P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="1%">&nbsp;</TD>
<TD WIDTH="2%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">a trust that (1)&nbsp;is subject to the primary supervision of a U.S. court and the control of one or more
&#147;United States persons&#148; (within the meaning of Section&nbsp;7701(a)(30) of the Code) or (2)&nbsp;has a valid election in effect to be treated as a United States person for U.S. federal income tax purposes. </P></TD></TR></TABLE>
<P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B><I>Stated Interest </I></B></P> <P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Stated interest
on a note generally will be taxable to a U.S. Holder as ordinary income at the time such interest is received or accrued, in accordance with such U.S. Holder&#146;s regular method of tax accounting for U.S. federal income tax purposes. </P>
<P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B><I>Sale or Other Taxable Disposition </I></B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">A U.S. Holder will recognize gain or loss (if any) on a sale, exchange, redemption, retirement or other taxable disposition of a note. The
amount of such gain or loss will generally be equal to the difference between the amount received for the note in cash or other property valued at fair market value (less amounts attributable </P>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">S-41 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman">
to any accrued but unpaid stated interest, which will be taxable as ordinary income to the extent not previously included in income) and the U.S. Holder&#146;s adjusted tax basis in the note. A
U.S. Holder&#146;s adjusted tax basis in a note generally will be equal to the amount the U.S. Holder paid for the note. Any such gain or loss will be capital gain or loss, and will be long-term capital gain or loss if the U.S. Holder has held the
note for more than one year at the time of the sale or other taxable disposition. Otherwise, such gain or loss will be short-term capital gain or loss. Long-term capital gains recognized by <FONT STYLE="white-space:nowrap">non-corporate</FONT> U.S.
Holders, including individuals, generally will be taxable at a reduced rate. The deductibility of capital losses is subject to limitations. </P>
<P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B><I>Information Reporting and Backup Withholding </I></B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">A U.S. Holder may be subject to information reporting and backup withholding with respect to payments of stated interest on a note and proceeds
from the sale or other taxable disposition of a note (including a redemption or retirement of a note). Certain U.S. Holders are exempt from backup withholding, including corporations and certain <FONT STYLE="white-space:nowrap">tax-exempt</FONT>
organizations. A U.S. Holder will be subject to backup withholding if such holder is not otherwise exempt and: </P> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="1%">&nbsp;</TD>
<TD WIDTH="2%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the holder fails to furnish the holder&#146;s taxpayer identification number, which for an individual is
ordinarily his or her social security number; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="1%">&nbsp;</TD>
<TD WIDTH="2%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the holder furnishes an incorrect taxpayer identification number; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="1%">&nbsp;</TD>
<TD WIDTH="2%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the applicable withholding agent is notified by the IRS that the holder has become subject to backup withholding
due to a prior failure to properly report payments of interest or dividends; or </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="1%">&nbsp;</TD>
<TD WIDTH="2%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the holder fails to certify under penalties of perjury that the holder has furnished a correct taxpayer
identification number and that the IRS has not notified the holder that the holder is subject to backup withholding. </P></TD></TR></TABLE>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Backup withholding is not an additional tax. Any amounts withheld under the backup withholding rules may be allowed as a refund or a credit
against a U.S. Holder&#146;s U.S. federal income tax liability, provided the required information is timely furnished to the IRS. U.S. Holders should consult their tax advisors regarding their qualification for an exemption from backup withholding
and the procedures for obtaining such an exemption. </P> <P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B>Tax Consequences Applicable to <FONT STYLE="white-space:nowrap">Non-U.S.</FONT> Holders </B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B><I>Definition of a <FONT STYLE="white-space:nowrap">Non-U.S.</FONT> Holder </I></B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">For purposes of this discussion, a <FONT STYLE="white-space:nowrap">&#147;Non-U.S.</FONT> Holder&#148; is a beneficial owner of a note that is
neither a U.S. Holder nor treated as a partnership for U.S. federal income tax purposes. </P> <P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B><I>Payments of Interest </I></B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Subject to the discussions below under &#147;&#151;Information Reporting and Backup Withholding&#148; and &#147;&#151;Additional Withholding
Tax on Payments Made to Foreign Accounts,&#148; interest paid on a note to a <FONT STYLE="white-space:nowrap">Non-U.S.</FONT> Holder that is not effectively connected with the <FONT STYLE="white-space:nowrap">Non-U.S.</FONT> Holder&#146;s conduct of
a trade or business within the United States generally will not be subject to U.S. federal income tax, or U.S. federal withholding tax, provided that: </P> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="1%">&nbsp;</TD>
<TD WIDTH="2%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the <FONT STYLE="white-space:nowrap">Non-U.S.</FONT> Holder does not, actually or constructively, own stock
possessing 10% or more of the total combined voting power of all classes of our voting stock; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="1%">&nbsp;</TD>
<TD WIDTH="2%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the <FONT STYLE="white-space:nowrap">Non-U.S.</FONT> Holder is not a controlled foreign corporation related to us
through actual or constructive stock ownership; and </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="1%">&nbsp;</TD>
<TD WIDTH="2%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">either (1)&nbsp;the <FONT STYLE="white-space:nowrap">Non-U.S.</FONT> Holder certifies in a statement provided to
the applicable withholding agent under penalties of perjury that it is not a United States person and provides its name and address; (2)&nbsp;a securities clearing organization, bank or other financial institution that holds customers&#146;
securities in </P></TD></TR></TABLE>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">S-42 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">

<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="9%">&nbsp;</TD>
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">
the ordinary course of its trade or business and holds the note on behalf of the <FONT STYLE="white-space:nowrap">Non-U.S.</FONT> Holder certifies to the applicable withholding agent under
penalties of perjury that it, or the financial institution between it and the <FONT STYLE="white-space:nowrap">Non-U.S.</FONT> Holder, has received from the <FONT STYLE="white-space:nowrap">Non-U.S.</FONT> Holder a statement under penalties of
perjury that such holder is not a United States person and provides a copy of such statement to the applicable withholding agent; or (3)&nbsp;the <FONT STYLE="white-space:nowrap">Non-U.S.</FONT> Holder holds its note directly through a
&#147;qualified intermediary&#148; (within the meaning of applicable Treasury Regulations) and certain conditions are satisfied. </P></TD></TR></TABLE>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">If a <FONT STYLE="white-space:nowrap">Non-U.S.</FONT> Holder does not satisfy the requirements above, interest paid to such <FONT
STYLE="white-space:nowrap">Non-U.S.</FONT> Holder that is not effectively connected with the conduct of a trade or business within the United States will generally be subject to a 30% U.S. federal withholding tax, subject to a reduction in or an
exemption from withholding on such interest as a result of an applicable income tax treaty. To claim such entitlement, the <FONT STYLE="white-space:nowrap">Non-U.S.</FONT> Holder must provide the applicable withholding agent with a properly executed
IRS Form <FONT STYLE="white-space:nowrap">W-8BEN</FONT> or <FONT STYLE="white-space:nowrap"><FONT STYLE="white-space:nowrap">W-8BEN-E,</FONT></FONT> as applicable (or other applicable documentation) claiming a reduction in or exemption from
withholding tax under the benefit of an applicable income tax treaty between the United States and the country in which the <FONT STYLE="white-space:nowrap">Non-U.S.</FONT> Holder resides or is established. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">If interest paid to a <FONT STYLE="white-space:nowrap">Non-U.S.</FONT> Holder is effectively connected with the
<FONT STYLE="white-space:nowrap">Non-U.S.</FONT> Holder&#146;s conduct of a trade or business within the United States, unless an applicable income tax treaty provides otherwise, the <FONT STYLE="white-space:nowrap">Non-U.S.</FONT> Holder will be
exempt from the U.S. federal withholding tax described above. To claim the exemption, the <FONT STYLE="white-space:nowrap">Non-U.S.</FONT> Holder generally must furnish to the applicable withholding agent a valid IRS Form <FONT
STYLE="white-space:nowrap">W-8ECI</FONT> (or other applicable documentation), certifying that interest paid on a note is not subject to withholding tax because it is effectively connected with the conduct by the
<FONT STYLE="white-space:nowrap">Non-U.S.</FONT> Holder of a trade or business within the United States. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Unless an applicable income tax
treaty provides otherwise, any such effectively connected interest generally will be subject to U.S. federal income tax on a net income basis at the regular rates of tax. A <FONT STYLE="white-space:nowrap">Non-U.S.</FONT> Holder that is a
corporation also may be subject to a branch profits tax at a rate of 30% (or such lower rate specified by an applicable income tax treaty) on its effectively connected earnings and profits (including effectively connected interest), as adjusted for
certain items. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The certifications described above must be provided to the applicable withholding agent prior to the payment of interest
and must be updated periodically. <FONT STYLE="white-space:nowrap">Non-U.S.</FONT> Holders that do not timely provide the applicable withholding agent with the required certification, but that qualify for a reduced rate under an applicable income
tax treaty, may obtain a refund of any excess amounts withheld by timely filing an appropriate claim for refund with the IRS. <FONT STYLE="white-space:nowrap">Non-U.S.</FONT> Holders should consult their tax advisors regarding their entitlement to
benefits under any applicable income tax treaty. </P> <P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B><I>Sale or Other Taxable Disposition </I></B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Subject to the discussions below under &#147;&#151;Information Reporting and Backup Withholding&#148; and &#147;&#151; Additional Withholding
Tax on Payments Made to Foreign Accounts,&#148; a <FONT STYLE="white-space:nowrap">Non-U.S.</FONT> Holder will not be subject to U.S. federal income tax on any gain recognized upon the sale, exchange, redemption, retirement or other taxable
disposition of a note (other than amounts allocable to any accrued and unpaid interest, which generally will be treated as interest and may be subject to the rules discussed above in &#147;&#151;Payments of Interest&#148;) unless: </P>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="1%">&nbsp;</TD>
<TD WIDTH="2%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the gain is effectively connected with the <FONT STYLE="white-space:nowrap">Non-U.S.</FONT> Holder&#146;s conduct
of a trade or business within the United States; or </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="1%">&nbsp;</TD>
<TD WIDTH="2%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the <FONT STYLE="white-space:nowrap">Non-U.S.</FONT> Holder is a
<FONT STYLE="white-space:nowrap">non-resident</FONT> alien individual present in the United States for 183 days or more during the taxable year of the disposition and certain other requirements are met. </P></TD></TR></TABLE>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Unless an applicable income tax treaty provides otherwise, any gain described in the first bullet point above generally will be subject to
U.S. federal income tax on a net income basis at the regular graduated rates. A </P>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">S-43 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman">
<FONT STYLE="white-space:nowrap">Non-U.S.</FONT> Holder that is a corporation also may be subject to a branch profits tax at a rate of 30% (or such lower rate specified by an applicable income
tax treaty) on its effectively connected earnings and profits (including effectively connected gain), as adjusted for certain items. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Any
gain described in the second bullet point above will be subject to U.S. federal income tax at a rate of 30% (or such lower rate specified by an applicable income tax treaty), which gain may be offset by certain U.S. source capital losses of the <FONT
STYLE="white-space:nowrap">Non-U.S.</FONT> Holder, if any (even though the individual is not considered a resident of the United States), provided the <FONT STYLE="white-space:nowrap">Non-U.S.</FONT> Holder has timely filed U.S. federal income tax
returns with respect to such losses. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman"><FONT STYLE="white-space:nowrap">Non-U.S.</FONT> Holders should consult their tax advisors regarding
any applicable income tax treaties that may provide for different rules. </P> <P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B><I>Information Reporting and Backup Withholding </I></B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Payments of interest to a <FONT STYLE="white-space:nowrap">Non-U.S.</FONT> Holder generally will not be subject to backup withholding, provided
the applicable withholding agent does not have actual knowledge or reason to know the holder is a United States person and the holder certifies its <FONT STYLE="white-space:nowrap">non-U.S.</FONT> status as described above under &#147;&#151;Payments
of Interest&#148; or otherwise establishes an exemption. However, information returns are required to be filed with the IRS in connection with any interest paid to the <FONT STYLE="white-space:nowrap">Non-U.S.</FONT> Holder, regardless of whether
any tax was actually withheld. In addition, proceeds of the sale or other taxable disposition of a note (including a retirement or redemption of the note) paid to or through the U.S.&nbsp;office of a broker or the
<FONT STYLE="white-space:nowrap">non-U.S.</FONT> office of a broker that is a U.S. person, or a <FONT STYLE="white-space:nowrap">non-U.S.</FONT> person with specified connections to the United States, generally will not be subject to backup
withholding or information reporting if the applicable withholding agent receives the statement described above and does not have actual knowledge, or reason to know that such holder is a United States person or the holder otherwise establishes an
exemption. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Proceeds of a disposition of a note paid to or through a <FONT STYLE="white-space:nowrap">non-U.S.</FONT> office of a broker
that is a <FONT STYLE="white-space:nowrap">non-U.S.</FONT> person without specified connections to the United States generally will not be subject to backup withholding or information reporting. Copies of information returns that are filed with the
IRS may also be made available under the provisions of an applicable treaty or agreement to the tax authorities of the country in which the <FONT STYLE="white-space:nowrap">Non-U.S.</FONT> Holder resides or is established. Backup withholding is not
an additional tax. Any amounts withheld under the backup withholding rules may be allowed as a refund or a credit against a <FONT STYLE="white-space:nowrap">Non-U.S.</FONT> Holder&#146;s U.S. federal income tax liability, if any, provided the
required information is timely furnished to the IRS. </P> <P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B>Additional Withholding Tax on Payments Made to Foreign Accounts </B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Withholding taxes may be imposed under Sections 1471 through 1474 of the Code (commonly referred to as the Foreign Account Tax Compliance Act,
or &#147;FATCA&#148;) on certain types of payments made to <FONT STYLE="white-space:nowrap">non-U.S.</FONT> financial institutions and certain other <FONT STYLE="white-space:nowrap">non-U.S.</FONT> entities. Specifically, a 30% withholding tax may
be imposed on payments of stated interest on, or (subject to the proposed Treasury Regulations discussed below) gross proceeds from the sale or other taxable disposition (including a retirement or redemption) of, a note paid to a &#147;foreign
financial institution&#148; or a <FONT STYLE="white-space:nowrap">&#147;non-financial</FONT> foreign entity&#148; (each as defined in the Code), whether such institution or entity is the beneficial owner or an intermediary, unless (1)&nbsp;the
foreign financial institution undertakes certain diligence and reporting obligations, (2)&nbsp;the <FONT STYLE="white-space:nowrap">non-financial</FONT> foreign entity either certifies it does not have any &#147;substantial United States
owners&#148; (as defined in the Code) or furnishes identifying information regarding each substantial United States owner, or (3)&nbsp;the foreign financial institution or <FONT STYLE="white-space:nowrap">non-financial</FONT> foreign entity
otherwise qualifies for an exemption from these rules. If the payee is a foreign financial institution and is subject to the diligence and reporting requirements in (1)&nbsp;above, it must enter into an agreement with the U.S. Department of the
Treasury requiring, among other things, that it undertake to identify accounts held by certain &#147;specified United States persons&#148; or &#147;United States owned foreign entities&#148; (each as defined in the Code), annually report
</P>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">S-44 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman">
certain information about such accounts, and withhold 30% on certain payments to <FONT STYLE="white-space:nowrap">non-compliant</FONT> foreign financial institutions and certain other account
holders. Foreign financial institutions located in jurisdictions that have an intergovernmental agreement with the United States governing FATCA may be subject to different rules. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Under the applicable Treasury Regulations and administrative guidance, withholding under FATCA generally applies to payments of interest on a
note. While withholding under FATCA would also have applied to payments of gross proceeds from the sale or other taxable disposition of a note, proposed Treasury Regulations eliminate FATCA withholding on payments of gross proceeds entirely.
Taxpayers generally may rely on these proposed Treasury Regulations until final Treasury Regulations are issued. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Prospective investors
should consult their tax advisors regarding the potential application of withholding under FATCA to their investment in the notes. </P>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">S-45 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center"><B><A NAME="supprom326517_10"></A>UNDERWRITING (CONFLICTS OF INTEREST) </B></P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">BofA Securities, Inc. and Wells Fargo Securities, LLC are acting as representatives of each of the underwriters named below. Subject to the
terms and conditions set forth in a firm commitment underwriting agreement among us and the underwriters, we have agreed to sell to the underwriters, and each of the underwriters has agreed, severally and not jointly, to purchase from us, the
principal amount of notes set forth opposite its name below. </P> <P STYLE="font-size:12pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE CELLSPACING="0" CELLPADDING="0" WIDTH="100%" BORDER="0" STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" ALIGN="center">


<TR>

<TD WIDTH="58%"></TD>

<TD VALIGN="bottom" WIDTH="3%"></TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TD VALIGN="bottom" WIDTH="3%"></TD>
<TD></TD>
<TD></TD>
<TD></TD>

<TD VALIGN="bottom" WIDTH="3%"></TD>
<TD></TD>
<TD></TD>
<TD></TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:8pt">
<TD VALIGN="bottom"><B>Underwriter</B></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="bottom" COLSPAN="2" ALIGN="center" STYLE="border-bottom:1.00pt solid #000000"><B>Principal&nbsp;Amount<BR>of&nbsp;2024&nbsp;Notes</B></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="bottom" COLSPAN="2" ALIGN="center" STYLE="border-bottom:1.00pt solid #000000"><B>Principal&nbsp;Amount<BR>of 2032 Notes</B></TD>
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="bottom" COLSPAN="2" ALIGN="center" STYLE="border-bottom:1.00pt solid #000000"><B>Principal&nbsp;Amount<BR>of 2041 Notes</B></TD>
<TD VALIGN="bottom">&nbsp;</TD></TR>


<TR BGCOLOR="#cceeff" STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">BofA Securities, Inc.</P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">125,000,000</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">125,000,000</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">125,000,000</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">Wells Fargo Securities, LLC</P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">125,000,000</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">125,000,000</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">125,000,000</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR BGCOLOR="#cceeff" STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">J.P. Morgan Securities LLC</P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">47,500,000</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">47,500,000</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">47,500,000</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">PNC Capital Markets LLC</P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">47,500,000</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">47,500,000</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">47,500,000</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR BGCOLOR="#cceeff" STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">Truist Securities, Inc.</P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">47,500,000</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">47,500,000</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">47,500,000</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">BBVA Securities Inc.</P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">17,500,000</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">17,500,000</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">17,500,000</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR BGCOLOR="#cceeff" STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">BMO Capital Markets Corp.</P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">17,500,000</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">17,500,000</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">17,500,000</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">BNP Paribas Securities Corp.</P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">17,500,000</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">17,500,000</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">17,500,000</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR BGCOLOR="#cceeff" STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">Citizens Capital Markets, Inc.</P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">17,500,000</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">17,500,000</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">17,500,000</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">MUFG Securities Americas Inc.</P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">17,500,000</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">17,500,000</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">17,500,000</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR BGCOLOR="#cceeff" STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">HSBC Securities (USA) Inc.</P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">10,000,000</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">10,000,000</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">10,000,000</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">U.S. Bancorp Investments, Inc.</P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">10,000,000</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">10,000,000</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">10,000,000</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="font-size:1px; ">
<TD VALIGN="bottom"></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD>&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD>&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:1.00px solid #000000">&nbsp;</P></TD>
<TD>&nbsp;</TD></TR>
<TR BGCOLOR="#cceeff" STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:3.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman">Total</P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">500,000,000</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">500,000,000</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">$</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">500,000,000</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="font-size:1px; ">
<TD VALIGN="bottom"></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:3.00px double #000000">&nbsp;</P></TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:3.00px double #000000">&nbsp;</P></TD>
<TD>&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:3.00px double #000000">&nbsp;</P></TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:3.00px double #000000">&nbsp;</P></TD>
<TD>&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:3.00px double #000000">&nbsp;</P></TD>
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; border-top:3.00px double #000000">&nbsp;</P></TD>
<TD>&nbsp;</TD></TR>
</TABLE> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Subject to the terms and conditions set forth in the underwriting agreement, the underwriters have agreed,
severally and not jointly, to purchase all of the notes sold under the underwriting agreement if any of these notes are purchased. If an underwriter defaults, the underwriting agreement provides that the purchase commitments of the <FONT
STYLE="white-space:nowrap">non-defaulting</FONT> underwriters may be increased or the underwriting agreement may be terminated. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">We have
agreed to indemnify the underwriters and their controlling persons against certain liabilities in connection with this offering, including liabilities under the Securities Act of 1933, as amended (the &#147;Securities Act&#148;), or to contribute to
payments the underwriters may be required to make in respect of those liabilities. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The underwriters are offering the notes, subject to
prior sale, when, as and if issued to and accepted by them, subject to approval of legal matters by their counsel, including the validity of the notes, and other conditions contained in the underwriting agreement, such as the receipt by the
underwriters of officer&#146;s certificates and legal opinions. The underwriters reserve the right to withdraw, cancel or modify offers to the public and to reject orders in whole or in part. </P>
<P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B>Commissions and Discounts </B></P> <P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The
representatives have advised us that the underwriters propose initially to offer the notes to the public at the public offering price set forth on the cover page of this prospectus supplement and to certain dealers at such price less a concession
not in excess of 0.20% of the principal amount of the 2024 notes, 0.40% of the principal amount of the 2032 notes and 0.525% of the principal amount of the 2041 notes. After the initial offering, the public offering price, concession or any other
term of the offering may be changed. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The expenses of the offering, not including the underwriting discount, are estimated at $3.9 million
and are payable by us. </P> <P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B>New Issues of Notes </B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The notes are new issues of securities with no established trading market. We do not intend to apply for listing of the notes on any national
securities exchange or for inclusion of the notes on any automated dealer quotation system. We have been advised by the underwriters that they presently intend to make a market in the notes after completion of the offering. However, they are under
no obligation to do so and may discontinue any market-making activities at any time without any notice. We cannot assure the liquidity of the trading market for </P>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">S-46 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman">
the notes or that an active public market for the notes will develop. If an active public trading market for the notes does not develop, the market price and liquidity of the notes may be
adversely affected. If the notes are traded, they may trade at a discount from their initial offering price, depending on prevailing interest rates, the market for similar securities, our operating performance and financial condition, general
economic conditions and other factors. </P> <P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B>Settlement </B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">We expect that delivery of the notes will be made to investors on or about September 23, 2021, which will be the tenth business day following
the date of this prospectus supplement (such settlement being referred to as &#147;T+10&#148;). Under Rule <FONT STYLE="white-space:nowrap">15c6-1</FONT> under the Exchange Act, trades in the secondary market are required to settle in two business
days, unless the parties to any such trade expressly agree otherwise. Accordingly, purchasers who wish to trade notes prior to the second business day before the delivery of the notes hereunder will be required, by virtue of the fact that the notes
initially settle in T+10, to specify an alternate settlement arrangement at the time of any such trade to prevent a failed settlement. Purchasers of the notes who wish to trade the notes prior to their date of delivery hereunder should consult their
advisors. </P> <P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B>No Sales of Similar Securities </B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">We have agreed that we will not, for the period following the date of this prospectus supplement through the closing date of the notes offered
hereby without first obtaining the prior written consent of BofA Securities, Inc. and Wells Fargo Securities, LLC, (i)&nbsp;directly or indirectly, offer, pledge, sell, contract to sell, sell any option or contract to purchase, purchase any option
or contract to sell, grant any option, right or warrant for the sale of, or lend or otherwise transfer or dispose of, the notes or any securities that are substantially similar to the notes, whether owned as of the date hereof or hereafter acquired
or with respect to which such person has or hereafter acquires the power of disposition, or file, or cause to be filed, any registration statement under the Securities Act with respect to any of the foregoing or (ii)&nbsp;enter into any swap or any
other agreement or any transaction that transfers, in whole or in part, directly or indirectly, the economic consequence of ownership of the notes or such other securities, whether any such transaction, swap or other agreement described in clause
(i)&nbsp;or (ii)&nbsp;above is to be settled by delivery of any notes or such other securities, in cash or otherwise, except for the notes sold to the underwriters pursuant to the underwriting agreement. </P>
<P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B>Short Positions </B></P> <P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">In connection with the
offering, the underwriters may purchase and sell the notes in the open market. These transactions may include short sales and purchases on the open market to cover positions created by short sales. Short sales involve the sale by the underwriters of
a greater principal amount of notes than they are required to purchase in the offering. The underwriters must close out any short position by purchasing notes in the open market. A short position is more likely to be created if the underwriters are
concerned that there may be downward pressure on the price of the notes in the open market after pricing that could adversely affect investors who purchase in the offering. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Similar to other purchase transactions, the underwriters&#146; purchases to cover the syndicate short sales may have the effect of raising or
maintaining the market price of the notes or preventing or retarding a decline in the market price of the notes. As a result, the price of the notes may be higher than the price that might otherwise exist in the open market. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Neither we nor any of the underwriters make any representation or prediction as to the direction or magnitude of any effect that the
transactions described above may have on the price of the notes. In addition, neither we nor any of the underwriters make any representation that the representatives will engage in these transactions or that these transactions, once commenced, will
not be discontinued without notice. </P> <P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B>Conflict of Interest </B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Affiliates of BofA Securities, Inc. and Wells Fargo Securities LLC have provided commitments under the Bridge Facility. In the event that the
Bridge Facility is funded prior to completion of this offering, we will be </P>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">S-47 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman">
required to use the net proceeds of this offering to prepay the amounts outstanding under the Bridge Facility on a
<FONT STYLE="white-space:nowrap"><FONT STYLE="white-space:nowrap">dollar-for-dollar</FONT></FONT> basis. As such, at least 5% or more of the net proceeds of this offering (not including underwriting discounts) may be directed to one or more of the
underwriters or their affiliates. The receipt of at least 5% of the net proceeds of this offering by any underwriter (or its affiliates) would be considered a &#147;conflict of interest&#148; under FINRA Rule 5121 regarding the underwriting of
securities of a company with a member that has a conflict of interest within the meaning of those rules. Pursuant to that rule, the appointment of a &#147;qualified independent underwriter&#148; (as such term is defined in FINRA Rule 5121) is not
necessary in connection with this offering as the securities offered are investment grade rated, as that term is defined in the rule. In accordance with FINRA Rule 5121, the underwriters with a conflict of interest will not confirm sales of notes to
any account over which they exercise discretionary authority without prior written approval of the customer. </P> <P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B>Other Relationships </B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Some of the underwriters and their affiliates have engaged in, and may in the future engage in, investment banking and other commercial
dealings in the ordinary course of business with us or our affiliates. They have received, or may in the future receive, customary fees and commissions for these transactions. The underwriters and/or their affiliates are lenders and/or agents under
our credit facilities or serve as a broker in executing stock repurchases, or both. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">In addition, in the ordinary course of their business
activities, the underwriters and their affiliates may make or hold a broad array of investments and actively trade debt and equity securities (or related derivative securities) and financial instruments (including bank loans) for their own account
and for the accounts of their customers. Such investments and securities activities may involve securities and/or instruments of ours or our affiliates. If any of the underwriters or their affiliates has a lending relationship with us, certain of
those underwriters or their affiliates routinely hedge, and certain other of those underwriters may hedge, their credit exposure to us consistent with their customary risk management policies.&nbsp;Typically, such underwriters and their affiliates
would hedge such exposure by entering into transactions which consist of either the purchase of credit default swaps or the creation of short positions in our&nbsp;securities, including potentially the notes offered hereby.&nbsp;Any such credit
default swaps or short positions could adversely affect future trading prices of the notes offered hereby. The underwriters and their affiliates may also make investment recommendations and/or publish or express independent research views in respect
of such securities or financial instruments and may hold, or recommend to clients that they acquire, long and/or short positions in such securities and instruments. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Additionally, U.S. Bank National Association, an affiliate of U.S. Bancorp Investments, Inc., is trustee for the notes offered hereby. </P>
<P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B>European Economic Area </B></P> <P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The notes are not
intended to be offered, sold or otherwise made available to and should not be offered, sold or otherwise made available to any retail investor in the European Economic Area (&#147;EEA&#148;). For these purposes, a retail investor means a person who
is one (or more) of: (i)&nbsp;a retail client as defined in point (11)&nbsp;of Article 4(1) of Directive 2014/65/EU&nbsp;(as amended, &#147;MiFID II&#148;); or (ii)&nbsp;a customer within the meaning of Directive (EU) 2016/97 (as amended, the
&#147;Insurance Distribution Directive&#148;), where that customer would not qualify as a professional client as defined in point (10)&nbsp;of Article 4(1) of MiFID II; or (iii)&nbsp;not a qualified investor as defined in Regulation (EU) 2017/1129
(as amended, the &#147;Prospectus Regulation&#148;). Consequently no key information document required by Regulation (EU) No 1286/2014 (as amended, the &#147;PRIIPs Regulation&#148;) for offering or selling the notes or otherwise making them
available to retail investors in the EEA has been prepared and therefore offering or selling the notes or otherwise making them available to any retail investor in the EEA may be unlawful under the PRIIPs Regulation.&nbsp;This prospectus supplement
has been prepared on the basis that any offer of notes in any Member State of the EEA will be made pursuant to an exemption under the Prospectus Regulation from the requirement to publish a prospectus for offers of notes. This prospectus supplement
is not a prospectus for the purposes of the Prospectus Regulation. </P>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">S-48 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The above selling restriction is in addition to any other selling restrictions set out
below. </P> <P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B>Notice to Prospective Investors in the United Kingdom </B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The notes are not intended to be offered, sold or otherwise made available to and should not be offered, sold or otherwise made available to
any retail investor in the United Kingdom (&#147;UK&#148;). For these purposes, a retail investor means a person who is one (or more) of (i)&nbsp;a retail client, as defined in point (8)&nbsp;of Article 2 of Regulation (EU) 2017/565 as it forms part
of domestic law by virtue of the European Union (Withdrawal) Act 2018 (&#147;EUWA&#148;); or (ii)&nbsp;a customer within the meaning of the provisions of the Financial Services and Markets Act 2000 (as amended, the &#147;FSMA&#148;) and any rules or
regulations made under the FSMA to implement Directive (EU) 2016/97, where that customer would not qualify as a professional client, as defined in point (8)&nbsp;of Article 2(1) of Regulation (EU) 600/2014 as it forms part of domestic law by virtue
of the EUWA; or (iii)&nbsp;not a qualified investor as defined in Regulation (EU) 2017/1129 as it forms part of domestic law by virtue of the EUWA (the &#147;UK Prospectus Regulation&#148;). Consequently no key information document required by
Regulation (EU) 1286/2014 as it forms part of domestic law by virtue of the EUWA (the &#147;UK PRIIPs Regulation&#148;) for offering or selling the notes or otherwise making them available to retail investors in the UK has been prepared and
therefore offering or selling the notes or otherwise making them available to any retail investor in the UK may be unlawful under the UK PRIIPs Regulation. This prospectus supplement has been prepared on the basis that any offer of notes in the UK
will be made pursuant to an exemption under the UK Prospectus Regulation and the FSMA from the requirement to publish a prospectus for offers of notes. This prospectus supplement is not a prospectus for the purposes of the UK Prospectus Regulation
or the FSMA. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">This prospectus supplement is for distribution only to persons who (i)&nbsp;have professional experience in matters relating
to investments and who qualify as investment professionals within the meaning of Article 19(5) of the Financial Services and Markets Act 2000 (Financial Promotion) Order 2005 (as amended, the &#147;Financial Promotion Order&#148;), (ii) are persons
falling within Article 49(2)(a) to (d) (&#147;high net worth companies, unincorporated associations etc.&#148;) of the Financial Promotion Order, (iii)&nbsp;are outside the United Kingdom, or (iv)&nbsp;are persons to whom an invitation or inducement
to engage in investment activity (within the meaning of Section&nbsp;21 of the Financial Services and Markets Act 2000, as amended (&#147;FSMA&#148;)) in connection with the issue or sale of any securities may otherwise lawfully be communicated or
caused to be communicated (all such persons together being referred to as &#147;relevant persons&#148;). This prospectus supplement is directed only at relevant persons and must not be acted on or relied on by persons who are not relevant persons.
Any investment or investment activity to which this document relates is available only to relevant persons and will be engaged in only with relevant persons. </P>
<P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B>Notice to Prospective Investors in Switzerland </B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">This prospectus supplement is not intended to constitute an offer or solicitation to purchase or invest in the notes. The notes may not be
publicly offered, directly or indirectly, in Switzerland within the meaning of the Swiss Financial Services Act (&#147;FinSA&#148;) and no application has or will be made to admit the notes to trading on any trading venue (exchange or multilateral
trading facility) in Switzerland. Neither this prospectus supplement nor any other offering or marketing material relating to the notes constitutes a prospectus pursuant to the FinSA, and neither this prospectus supplement nor any other offering or
marketing material relating to the notes may be publicly distributed or otherwise made publicly available in Switzerland. </P> <P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B>Notice to Prospective
Investors in the Dubai International Financial Centre </B></P> <P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">This prospectus supplement relates to an Exempt Offer in accordance with the
Offered Securities Rules of the Dubai Financial Services Authority (&#147;DFSA&#148;). This prospectus supplement is intended for distribution only to persons of a type specified in the Offered Securities Rules of the DFSA. It must not be delivered
to, or relied on by, any other person. The DFSA has no responsibility for reviewing or verifying any documents in connection with Exempt Offers. The DFSA has not approved this prospectus supplement nor taken steps to verify the information set forth
herein and has no responsibility for the prospectus supplement. The notes to which this prospectus supplement relates may be illiquid and/or subject to restrictions on their resale. Prospective purchasers of the notes offered should conduct their
own due diligence on the notes. If you do not understand the contents of this prospectus supplement you should consult an authorized financial advisor. </P>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">S-49 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B>Notice to Prospective Investors in Canada </B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The notes may be sold only to purchasers purchasing, or deemed to be purchasing, as principal that are accredited investors, as defined in
National Instrument <FONT STYLE="white-space:nowrap">45-106</FONT> Prospectus Exemptions or subsection 73.3(1) of the Securities Act (Ontario), and are permitted clients, as defined in National Instrument
<FONT STYLE="white-space:nowrap">31-103</FONT> Registration Requirements, Exemptions and Ongoing Registrant Obligations. Any resale of the notes must be made in accordance with an exemption from, or in a transaction not subject to, the prospectus
requirements of applicable securities laws. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Securities legislation in certain provinces or territories of Canada may provide a purchaser
with remedies for rescission or damages if this prospectus supplement (including any amendment thereto) contains a misrepresentation, provided that the remedies for rescission or damages are exercised by the purchaser within the time limit
prescribed by the securities legislation of the purchaser&#146;s province or territory. The purchaser should refer to any applicable provisions of the securities legislation of the purchaser&#146;s province or territory for particulars of these
rights or consult with a legal advisor. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Pursuant to section 3A.3 of National Instrument <FONT STYLE="white-space:nowrap">33-105</FONT>
Underwriting Conflicts (NI <FONT STYLE="white-space:nowrap">33-105),</FONT> the underwriters are not required to comply with the disclosure requirements of NI <FONT STYLE="white-space:nowrap">33-105</FONT> regarding underwriter conflicts of interest
in connection with this offering. </P> <P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B>Notice to Prospective Investors in Australia </B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">No placement document, prospectus, product disclosure statement or other disclosure document has been lodged with the Australian Securities and
Investments Commission (&#147;ASIC&#148;), in relation to the offering. This prospectus supplement does not constitute a prospectus, product disclosure statement or other disclosure document under the Corporations Act 2001 (the &#147;Corporations
Act&#148;), and does not purport to include the information required for a prospectus, product disclosure statement or other disclosure document under the Corporations Act. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Any offer in Australia of the notes may only be made to persons (the &#147;Exempt Investors&#148;) who are &#147;sophisticated investors&#148;
(within the meaning of section 708(8) of the Corporations Act), &#147;professional investors&#148; (within the meaning of section 708(11) of the Corporations Act) or otherwise pursuant to one or more exemptions contained in section 708 of the
Corporations Act so that it is lawful to offer the notes without disclosure to investors under Chapter 6D of the Corporations Act. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The
notes applied for by Exempt Investors in Australia must not be offered for sale in Australia in the period of 12 months after the date of allotment under the offering, except in circumstances where disclosure to investors under Chapter 6D of the
Corporations Act would not be required pursuant to an exemption under section 708 of the Corporations Act or otherwise or where the offer is pursuant to a disclosure document which complies with Chapter 6D of the Corporations Act. Any person
acquiring notes must observe such Australian <FONT STYLE="white-space:nowrap">on-sale</FONT> restrictions. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">This prospectus supplement
contains general information only and does not take account of the investment objectives, financial situation or particular needs of any particular person. It does not contain any securities recommendations or financial product advice. Before making
an investment decision, investors need to consider whether the information in this prospectus supplement is appropriate to their needs, objectives and circumstances, and, if necessary, seek expert advice on those matters. </P>
<P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B>Notice to Prospective Investors in Hong Kong </B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The notes have not been offered or sold and will not be offered or sold in Hong Kong, by means of any document, other than (a)&nbsp;to
&#147;professional investors&#148; as defined in the Securities and Futures Ordinance </P>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">S-50 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman">
(Cap.&nbsp;571) of Hong Kong and any rules made under that Ordinance; or (b)&nbsp;in other circumstances which do not result in the document being a &#147;prospectus&#148; as defined in the
Companies Ordinance (Cap. 32) of Hong Kong or which do not constitute an offer to the public within the meaning of that Ordinance. No advertisement, invitation or document relating to the notes has been or may be issued or has been or may be in the
possession of any person for the purposes of issue, whether in Hong Kong or elsewhere, which is directed at, or the contents of which are likely to be accessed or read by, the public of Hong Kong (except if permitted to do so under the securities
laws of Hong Kong) other than with respect to notes which are or are intended to be disposed of only to persons outside Hong Kong or only to &#147;professional investors&#148; as defined in the Securities and Futures Ordinance and any rules made
under that Ordinance. </P> <P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B>Notice to Prospective Investors in Singapore </B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">This prospectus has not been registered as a prospectus with the Monetary Authority of Singapore. Accordingly, the notes were not offered or
sold or caused to be made the subject of an invitation for subscription or purchase and will not be offered or sold or caused to be made the subject of an invitation for subscription or purchase, and this prospectus or any other document or material
in connection with the offer or sale, or invitation for subscription or purchase, of the notes, has not been circulated or distributed, nor will it be circulated or distributed, whether directly or indirectly, to any person in Singapore other than
(i)&nbsp;to an institutional investor (as defined in Section&nbsp;4A of the Securities and Futures Act (Chapter 289) of Singapore, as modified or amended from time to time (the &#147;SFA&#148;)) pursuant to Section&nbsp;274 of the SFA, (ii)&nbsp;to
a relevant person (as defined in Section&nbsp;275(2) of the SFA) pursuant to Section&nbsp;275(1) of the SFA, or any person pursuant to Section&nbsp;275(1A) of the SFA, and in accordance with the conditions specified in Section&nbsp;275 of the SFA,
or (iii)&nbsp;otherwise pursuant to, and in accordance with the conditions of, any other applicable provision of the SFA. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Where the notes
are subscribed or purchased under Section&nbsp;275 of the SFA by a relevant person which is: </P> <P STYLE="margin-top:6pt; margin-bottom:0pt; margin-left:4%; text-indent:4%; font-size:10pt; font-family:Times New Roman">(a) a corporation (which is
not an accredited investor (as defined in Section&nbsp;4A of the SFA)) the sole business of which is to hold investments and the entire share capital of which is owned by one or more individuals, each of whom is an accredited investor; or </P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; margin-left:4%; text-indent:4%; font-size:10pt; font-family:Times New Roman">(b) a trust (where the trustee is not an accredited investor) whose sole purpose is to hold investments and each beneficiary of
the trust is an individual who is an accredited investor, </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman">securities or securities-based derivatives contracts (each term as defined in Section&nbsp;2(1)
of the SFA) of that corporation or the beneficiaries&#146; rights and interest (howsoever described) in that trust shall not be transferred within six months after that corporation or that trust has acquired the notes pursuant to an offer made under
Section&nbsp;275 of the SFA except: </P> <P STYLE="margin-top:6pt; margin-bottom:0pt; margin-left:4%; text-indent:4%; font-size:10pt; font-family:Times New Roman">(a) to an institutional investor or to a relevant person, or to any person arising
from an offer referred to in Section&nbsp;275(1A) or Section&nbsp;276(4)(i)(B) of the SFA; </P> <P STYLE="margin-top:6pt; margin-bottom:0pt; margin-left:4%; text-indent:4%; font-size:10pt; font-family:Times New Roman">(b) where no consideration is
or will be given for the transfer; </P> <P STYLE="margin-top:6pt; margin-bottom:0pt; margin-left:4%; text-indent:4%; font-size:10pt; font-family:Times New Roman">(c) where the transfer is by operation of law; or </P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; margin-left:4%; text-indent:4%; font-size:10pt; font-family:Times New Roman">(d) as specified in Section&nbsp;276(7) of the SFA. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Singapore Securities and Futures Act Product Classification&#151;Solely for the purposes of its obligations pursuant to Sections 309B(1)(a)
and 309B(1)(c) of the SFA, the issuer has determined, and hereby notifies all relevant persons (as defined in Section&nbsp;309A of the SFA) that the notes are &#147;prescribed capital markets products&#148; (as defined in the Securities and Futures
(Capital Markets Products) Regulations 2018) and &#147;Excluded Investment Products&#148; (as defined in MAS Notice SFA <FONT STYLE="white-space:nowrap">04-N12:</FONT> Notice on the Sale of Investment Products and MAS Notice <FONT
STYLE="white-space:nowrap">FAA-N16:</FONT> Notice on Recommendations on Investment Products). </P>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">S-51 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B>Notice to Prospective Investors in Japan </B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The notes have not been and will not be registered under the Financial Instruments and Exchange Law of Japan (the Financial Instruments and
Exchange Law) and the underwriters have agreed that they will not offer or sell any notes, directly or indirectly, in Japan or to, or for the benefit of, any resident of Japan (which term as used herein means any person resident in Japan, including
any corporation or other entity organized under the laws of Japan), or to others for reoffering or resale, directly or indirectly, in Japan or to a resident of Japan, except pursuant to an exemption from the registration requirements of, and
otherwise in compliance with, the Financial Instruments and Exchange Law and any other applicable laws, regulations and ministerial guidelines of Japan. </P>
<P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B>Notice to Prospective Investors in Taiwan </B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The notes have not been and will not be registered with the Financial Supervisory Commission of Taiwan pursuant to relevant securities laws and
regulations and may not be sold, issued or offered within Taiwan through a public offering or in circumstances which constitutes an offer within the meaning of the Securities and Exchange Act of Taiwan that requires a registration or approval of the
Financial Supervisory Commission of Taiwan. No person or entity in Taiwan has been authorized to offer, sell, give advice regarding or otherwise intermediate the offering and sale of the notes in Taiwan. </P>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">S-52 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center"><B><A NAME="supprom326517_11"></A>LEGAL MATTERS </B></P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Certain legal matters in connection with the notes will be passed upon for us by Latham&nbsp;&amp; Watkins LLP, Houston, Texas, and Duane
Morris LLP, Houston, Texas. Certain legal matters in connection with the notes will be passed upon for the underwriters by Cahill Gordon&nbsp;&amp; Reindel LLP, New York, New York. </P>
<P STYLE="margin-top:24pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center"><B><A NAME="supprom326517_12"></A>EXPERTS </B></P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The financial statements and management&#146;s assessment of the effectiveness of internal control over financial reporting (which is included
in Management&#146;s Report on Internal Control over Financial Reporting) incorporated in this prospectus by reference to the Annual Report on Form <FONT STYLE="white-space:nowrap">10-K</FONT> for the year ended December&nbsp;31, 2020 have been so
incorporated in reliance on the report (which contains an explanatory paragraph on the effectiveness of internal control over financial reporting due to the exclusion of certain elements of the internal control over financial reporting of seven
acquired businesses the registrant acquired during 2020) of PricewaterhouseCoopers LLP, an independent registered public accounting firm, given on the authority of said firm as experts in auditing and accounting. </P>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">S-53 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B>PROSPECTUS </B></P> <P STYLE="font-size:12pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<P STYLE="margin-top:0pt;margin-bottom:0pt" ALIGN="center">


<IMG SRC="https://ot-cdn.s3.us-west-2.amazonaws.com/filing/Archives/edgar/data/1050915/000119312521271415/g326517g12n84.jpg" ALT="LOGO">
 </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; font-size:24pt; font-family:Times New Roman" ALIGN="center"><B>Quanta Services, Inc. </B></P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; font-size:14pt; font-family:Times New Roman" ALIGN="center"><B>Common Stock </B></P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:14pt; font-family:Times New Roman" ALIGN="center"><B>Preferred
Stock </B></P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:14pt; font-family:Times New Roman" ALIGN="center"><B>Debt Securities </B></P>
<P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:14pt; font-family:Times New Roman" ALIGN="center"><B>Warrants </B></P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:14pt; font-family:Times New Roman" ALIGN="center"><B>Depositary
Shares </B></P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:14pt; font-family:Times New Roman" ALIGN="center"><B>Purchase Contracts </B></P>
<P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:14pt; font-family:Times New Roman" ALIGN="center"><B>Purchase Units </B></P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:14pt; font-family:Times New Roman" ALIGN="center"><B>Units
</B></P> <P STYLE="font-size:12pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P><center> <P STYLE="line-height:6.0pt;margin-top:0pt;margin-bottom:2pt;border-bottom:1.00pt solid #000000;width:21%">&nbsp;</P></center>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">We may offer and sell from time to time, together or separately, in one or more offerings, any combination of the securities listed above. The
securities we may offer may be convertible into or exercisable or exchangeable for other securities. We may offer and sell these securities from time to time in amounts, at prices and on terms to be determined by market conditions and other factors
at the time of the offerings. We may offer and sell these securities to or through one or more underwriters, dealers and agents, or directly to one or more purchasers, on a continuous or delayed basis. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">This prospectus provides you with a general description of these securities and the general manner in which we will offer and sell the
securities. Each time we offer and sell securities under this prospectus, we will provide a prospectus supplement that will contain specific information about the terms of that offering and the securities being offered. A prospectus supplement also
may add, update or change information contained in this prospectus. You should carefully read this prospectus and any accompanying prospectus supplement before you invest in any of our securities. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Our common stock is traded on the New York Stock Exchange (&#147;NYSE&#148;) under the symbol &#147;PWR.&#148; </P>
<P STYLE="font-size:12pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P><center> <P STYLE="line-height:6.0pt;margin-top:0pt;margin-bottom:2pt;border-bottom:1.00pt solid #000000;width:21%">&nbsp;</P></center>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:12pt; font-family:Times New Roman"><B>Investing in our securities involves risks. You should carefully review and consider the information under the heading &#147;<A HREF="#toc326517_3">Risk
 Factors</A>&#148; beginning on page&nbsp;2 of this prospectus and in any applicable prospectus supplement and under similar headings in the other documents incorporated by reference into this prospectus. </B></P>
<P STYLE="font-size:12pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P><center> <P STYLE="line-height:6.0pt;margin-top:0pt;margin-bottom:2pt;border-bottom:1.00pt solid #000000;width:21%">&nbsp;</P></center>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman"><B>NEITHER THE SECURITIES AND EXCHANGE COMMISSION NOR ANY STATE SECURITIES COMMISSION HAS APPROVED OR DISAPPROVED OF THESE SECURITIES OR
DETERMINED IF THIS PROSPECTUS IS TRUTHFUL OR COMPLETE. ANY REPRESENTATION TO THE CONTRARY IS A CRIMINAL OFFENSE. </B></P> <P STYLE="font-size:12pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P><center>
<P STYLE="line-height:6.0pt;margin-top:0pt;margin-bottom:2pt;border-bottom:1.00pt solid #000000;width:21%">&nbsp;</P></center> <P STYLE="margin-top:12pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center"><B>The date of
this prospectus is September&nbsp;14, 2020. </B></P>
</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center"><B>TABLE OF CONTENTS </B></P>
<P STYLE="font-size:12pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE CELLSPACING="0" CELLPADDING="0" WIDTH="100%" BORDER="0" STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" ALIGN="center">


<TR>

<TD WIDTH="95%"></TD>

<TD VALIGN="bottom" WIDTH="3%"></TD>
<TD></TD>
<TD></TD>
<TD></TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:8pt">
<TD VALIGN="bottom">&nbsp;</TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD VALIGN="bottom" COLSPAN="2" ALIGN="center"><B>Page</B></TD>
<TD VALIGN="bottom">&nbsp;</TD></TR>


<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><A HREF="#toc326517_1">ABOUT THIS PROSPECTUS</A></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">i</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><A HREF="#toc326517_2">ABOUT QUANTA SERVICES, INC.</A></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">1</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><A HREF="#toc326517_3">RISK FACTORS</A></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">2</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><A HREF="#toc326517_4">FORWARD-LOOKING STATEMENTS</A></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">3</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><A HREF="#toc326517_5">USE OF PROCEEDS</A></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">7</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><A HREF="#toc326517_6">DESCRIPTION OF CAPITAL STOCK</A></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">8</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><A HREF="#toc326517_7">DESCRIPTION OF DEBT SECURITIES</A></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">12</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><A HREF="#toc326517_8">DESCRIPTION OF WARRANTS</A></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">23</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><A HREF="#toc326517_9">DESCRIPTION OF DEPOSITARY SHARES</A></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">24</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><A HREF="#toc326517_10">DESCRIPTION OF PURCHASE CONTRACTS AND PURCHASE UNITS</A></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">25</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><A HREF="#toc326517_11">DESCRIPTION OF UNITS</A></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">26</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><A HREF="#toc326517_12">PLAN OF DISTRIBUTION</A></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">27</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><A HREF="#toc326517_13">LEGAL MATTERS</A></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">30</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><A HREF="#toc326517_14">EXPERTS</A></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">30</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><A HREF="#toc326517_15">WHERE YOU CAN FIND MORE INFORMATION</A></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">30</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
<TR STYLE="page-break-inside:avoid ; font-family:Times New Roman; font-size:10pt">
<TD VALIGN="bottom"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; margin-left:1.00em; text-indent:-1.00em; font-size:10pt; font-family:Times New Roman"><A HREF="#toc326517_16">INCORPORATION OF CERTAIN INFORMATION BY REFERENCE</A></P></TD>
<TD VALIGN="bottom">&nbsp;&nbsp;</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD>
<TD NOWRAP VALIGN="bottom" ALIGN="right">30</TD>
<TD NOWRAP VALIGN="bottom">&nbsp;</TD></TR>
</TABLE>
</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center"><B><A NAME="toc326517_1"></A>ABOUT THIS PROSPECTUS </B></P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman"><B>You should rely only on the information contained or incorporated by reference in this prospectus and any prospectus supplement and any
written communication from us or any underwriter specifying the final terms of a particular offering. We have not authorized anyone to provide you with information different from that contained or incorporated by reference in this prospectus or any
prospectus supplement. We take no responsibility for, and can provide no assurance as to the reliability of, any other information that others may give you. We are not making an offer of these securities in any state where the offer is not
permitted. </B></P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman"><B>You should assume that the information appearing in this prospectus, any prospectus supplement or any document
incorporated by reference or any written communication from us or any underwriter specifying the final terms of a particular offering is accurate only as of the date of the applicable documents, regardless of the time of delivery of this prospectus
or any sale of securities. Our business, financial condition, results of operations and prospects may have changed since that date. </B></P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">This prospectus is part of an automatic registration statement on Form <FONT STYLE="white-space:nowrap">S-3</FONT> that we have filed with the
Securities and Exchange Commission, as a &#147;well-known seasoned issuer&#148; as defined in Rule 405 under the Securities Act of 1933, as amended (the &#147;Securities Act&#148;). Under this shelf registration statement, we may offer and sell from
time to time, together or separately, in one or more offerings, any combination of the securities described in this prospectus. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">This
prospectus provides you with a general description of the securities we may offer and sell. Each time we sell securities pursuant to this prospectus, we will provide a prospectus supplement and, if applicable, a free writing prospectus that will
contain specific information about the offering and the terms of the particular securities to be offered. The prospectus supplement and any related free writing prospectus may also add, update or change information contained in this prospectus. If
there is any inconsistency between the information in this prospectus and in any prospectus supplement or free writing prospectus, you should rely on the information in that prospectus supplement or free writing prospectus, as applicable. You should
carefully read this prospectus, any prospectus supplement and any related free writing prospectus, together with the additional information described under the heading &#147;Where You Can Find More Information&#148; and &#147;Incorporation of
Certain Information by Reference&#148; before you invest. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The registration statement of which this prospectus is a part, including the
exhibits to the registration statement, provides additional information about us and the securities. Wherever references are made in this prospectus to information that will be included in a prospectus supplement, to the extent permitted by
applicable law, rules&nbsp;or regulations, we may instead include such information or add, update or change the information contained in this prospectus by means of a post-effective amendment to the registration statement of which this prospectus is
a part, through filings we make with the Securities and Exchange Commission that are incorporated by reference into this prospectus or by any other method as may then be permitted under applicable law, rules&nbsp;or regulations. The registration
statement, including the exhibits to the registration statement and any post-effective amendment thereto, can be obtained from the Securities and Exchange Commission, as described under the heading &#147;Where You Can Find More Information.&#148;
</P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">This prospectus contains summaries of certain provisions contained in some of the documents described herein, but reference is made to
the actual documents for complete information. All of the summaries are qualified in their entirety by reference to the actual documents. For additional information about our business, operations and financial results, please read the documents
incorporated by reference herein under the heading &#147;Incorporation of Certain Information by Reference.&#148; </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">As used in this
prospectus, the terms &#147;Quanta,&#148; &#147;the Company,&#148; &#147;we,&#148; &#147;our&#148; and &#147;us&#148; refer to Quanta Services, Inc. and its consolidated subsidiaries, except where the context otherwise requires or as otherwise
indicated. </P>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">i </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center"><B><A NAME="toc326517_2"></A>ABOUT QUANTA SERVICES, INC. </B></P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">We are a leading provider of specialty contracting services, delivering comprehensive infrastructure solutions for the electric and gas
utility, energy and communications industries in the United States, Canada, Australia and select other international markets. The performance of our business generally depends on our ability to obtain contracts with customers and to effectively
deliver the services provided under those contracts. The services we provide include the design, installation, upgrade, repair and maintenance of infrastructure within each of the industries we serve, such as electric power transmission and
distribution networks; substation facilities; gas utility systems; refinery, petrochemical and industrial facilities; pipeline transmission systems and facilities; and telecommunications and cable multi-system operator networks. Our customers
include many of the leading companies in the industries we serve, and we endeavor to develop and maintain strategic alliances and preferred service provider status with our customers. Our services are typically provided pursuant to master service
agreements, repair and maintenance contracts and fixed price and <FONT STYLE="white-space:nowrap">non-fixed</FONT> price installation contracts. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Our principal executive offices are located at 2800 Post Oak Boulevard, Suite 2600, Houston, Texas 77056. Our telephone number at that
location is (713) <FONT STYLE="white-space:nowrap">629-7600.</FONT> Our website is www.quantaservices.com. Information contained in our website is not incorporated by reference to this prospectus and you should not consider information contained in
our website as part of this prospectus. </P>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">1 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center"><B><A NAME="toc326517_3"></A>RISK FACTORS </B></P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">An investment in our securities involves a high degree of risk. You should carefully consider the risks described in our filings with the
Securities and Exchange Commission referred to under the heading &#147;Where You Can Find More Information,&#148; including our most recent annual report on Form <FONT STYLE="white-space:nowrap">10-K</FONT> and quarterly reports on Form <FONT
STYLE="white-space:nowrap">10-Q</FONT> and other reports and documents we file with the Securities and Exchange Commission that are incorporated by reference herein, together with all of the other information included in this prospectus and the
documents we incorporate by reference. If any of these risks were to occur, our business, financial condition, results of operations or cash flows could be adversely affected. You could lose all or part of your investment. When we offer and sell any
securities pursuant to a prospectus supplement, we may include additional risk factors relevant to that offering in the prospectus supplement. </P>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">2 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center"><B><A NAME="toc326517_4"></A>FORWARD-LOOKING STATEMENTS </B></P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">This prospectus includes &#147;forward-looking statements&#148; reflecting assumptions, expectations, projections, intentions or beliefs about
future events that are intended to qualify for the &#147;safe harbor&#148; from liability established by the Private Securities Litigation Reform Act of 1995. You can identify these statements by the fact that they do not relate strictly to
historical or current facts. They use words such as &#147;anticipate,&#148; &#147;estimate,&#148; &#147;project,&#148; &#147;forecast,&#148; &#147;may,&#148; &#147;will,&#148; &#147;should,&#148; &#147;could,&#148; &#147;expect,&#148;
&#147;believe,&#148; &#147;plan,&#148; &#147;intend&#148; and other words of similar meaning. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">In particular, these include, but are not
limited to, statements relating to the following: </P> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">projected revenues, net income, earnings per share, margins, cash flows, liquidity, weighted average shares
outstanding, capital expenditures, tax rates and other projections of operating or financial results; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">expectations regarding our business or financial outlook; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">expectations regarding opportunities, trends and economic and regulatory conditions in particular markets or
industries; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">expectations regarding the novel coronavirus disease
<FONT STYLE="white-space:nowrap">(&#147;COVID-19&#148;),</FONT> including the potential impact of the <FONT STYLE="white-space:nowrap">COVID-19</FONT> pandemic and of governmental responses to the pandemic on our business, operations, supply chain,
personnel, financial condition, results of operations, cash flows and liquidity; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">expectations regarding our plans and strategies, including plans, effects and other matters relating to the <FONT
STYLE="white-space:nowrap">COVID-19</FONT> pandemic and our exit, through potential sale or otherwise, from our Latin American operations; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the business plans or financial condition of our customers, including with respect to or as a result of the <FONT
STYLE="white-space:nowrap">COVID-19</FONT> pandemic; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the potential impact of commodity prices and commodity production volumes on our business, financial condition,
results of operations and cash flows and demand for our services; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the potential benefits from, and future performance of, acquired businesses and our investments, including a
joint venture in which we own a 50% interest, LUMA Energy, LLC, which was selected for a <FONT STYLE="white-space:nowrap">15-year</FONT> operation and maintenance agreement to operate, maintain and modernize the approximately <FONT
STYLE="white-space:nowrap">18,000-mile</FONT> electric transmission and distribution system in Puerto Rico; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">beliefs and assumptions about the collectability of receivables; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the expected value of contracts or intended contracts with customers, as well as the scope, services, term or
results of any awarded or expected projects; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the development of and opportunities with respect to future projects, including renewable energy projects and
larger electric transmission and pipeline projects; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">future capital allocation initiatives, including the amount, timing and strategies with respect to any future
stock repurchases, and expectations regarding the declaration, amount and timing of any future cash dividends; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the impact of existing or potential legislation or regulation; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">potential opportunities that may be indicated by bidding activity or similar discussions with customers;
</P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the future demand for and availability of labor resources in the industries we serve; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the expected realization of remaining performance obligations or backlog; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the expected outcome of pending or threatened legal proceedings; and </P></TD></TR></TABLE>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">3 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">

<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">possible recovery of pending or contemplated insurance claims, change orders and claims asserted against
customers or third parties. </P></TD></TR></TABLE> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">These forward-looking statements are not guarantees of future performance, involve or rely
on a number of risks, uncertainties, and assumptions that are difficult to predict or are beyond our control, and reflect management&#146;s beliefs and assumptions based on information available at the time the statements are made. We caution you
that actual outcomes and results may differ materially from what is expressed, implied or forecasted by our forward-looking statements and that any or all of our forward-looking statements may turn out to be inaccurate or incorrect. Those statements
can be affected by inaccurate assumptions and by known or unknown risks and uncertainties, including the following: </P> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">market, industry, economic, financial or political conditions outside our control, including weakness in the
capital markets or the ongoing and potential impact to financial markets and worldwide economic activity resulting from the <FONT STYLE="white-space:nowrap">COVID-19</FONT> pandemic and related governmental actions; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">quarterly variations in our operating and financial results, liquidity, financial condition, cash flows, capital
requirements, and reinvestment opportunities, including the ongoing and potential impact to our business, operations and supply chains resulting from the <FONT STYLE="white-space:nowrap">COVID-19</FONT> pandemic and related governmental actions;
</P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the severity, magnitude and duration of the <FONT STYLE="white-space:nowrap">COVID-19</FONT> pandemic, including
impacts of the pandemic and of business and governmental responses to the pandemic (e.g., <FONT STYLE="white-space:nowrap"><FONT STYLE="white-space:nowrap">shelter-in-place</FONT></FONT> and other mobility restrictions, business closures) on our
operations, personnel and supply chains, and on commercial activity and demand across our and our customers&#146; businesses; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">our inability to predict the extent to which the <FONT STYLE="white-space:nowrap">COVID-19</FONT> pandemic and
related impacts will adversely impact our business, financial performance, results of operations, financial position, the prices of our securities and the achievement of our strategic objectives, including with respect to governmental restrictions
on our ability to operate, workforce and key personnel availability, regulatory and permitting delays, and future demand for energy and the resulting impact on demand for our services; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">trends and growth opportunities in relevant markets, including our ability to obtain future project awards;
</P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the time and costs required to exit our Latin American operations and our ability to effect related transactions
on acceptable terms, as well as the business and political climate in Latin America; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">delays, deferrals, reductions in scope or cancellations of anticipated, pending or existing projects as a result
of, among other things, the <FONT STYLE="white-space:nowrap">COVID-19</FONT> pandemic, weather, regulatory or permitting issues (including the recent court ruling vacating the U.S. Army Corps of Engineers&#146; Nationwide Permit 12), environmental
processes, project performance issues, claimed force majeure events, protests or other political activity, legal challenges, reductions or eliminations in governmental funding or customer capital constraints; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the effect of commodity prices and commodity production volumes on our operations and growth opportunities and on
our customers&#146; capital programs and demand for our services, including as a result of the recent significant decrease in commodity prices; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the successful negotiation, execution, performance and completion of anticipated, pending and existing contracts;
</P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">risks associated with operational hazards that arise due to the nature of the services we provide and the
conditions in which we operate, including, among others, wildfires and explosions; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">unexpected costs, liabilities, fines or penalties that may arise from legal proceedings, indemnity obligations,
reimbursement obligations associated with letters of credit or bonds, multiemployer pension plans (e.g., underfunding of liabilities, termination or withdrawal liability) or other claims or actions asserted against us, including amounts that are not
covered by, or are in excess of, our third-party insurance; </P></TD></TR></TABLE>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">4 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">

<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">potential unavailability or cancellation of third-party insurance coverage, as well as the exclusion of coverage
for certain losses, potential increases in premiums for coverage deemed beneficial to us, or the unavailability of coverage deemed beneficial to us at reasonable and competitive rates; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">damage to our brands or reputation arising as a result of cyber-security breaches, environmental and occupational
health and safety matters, corporate scandal, failure to successfully perform a high-profile project, involvement in a catastrophic event (e.g., fire, explosion) or other negative incidents; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">our dependence on suppliers, subcontractors, equipment manufacturers and other third-party contractors and the
impact of the <FONT STYLE="white-space:nowrap">COVID-19</FONT> pandemic on these service providers; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">estimates and assumptions related to our financial results, remaining performance obligations and backlog;
</P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">our ability to attract and the potential shortage of skilled employees and our ability to retain key personnel
and qualified employees and the impact of the <FONT STYLE="white-space:nowrap">COVID-19</FONT> pandemic on the availability and performance of our workforce and key personnel; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">our dependence on fixed price contracts and the potential to incur losses with respect to these contracts;
</P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">adverse weather conditions, natural disasters and other emergencies, including wildfires, pandemics (including
the ongoing <FONT STYLE="white-space:nowrap">COVID-19</FONT> pandemic), hurricanes, tropical storms, floods, earthquakes and other geological- and weather-related hazards; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">our ability to generate internal growth; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">competition in our business, including our ability to effectively compete for new projects and market share;
</P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the future development of natural resources; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the failure of existing or potential legislative actions and initiatives to result in increased demand for our
services; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">fluctuations of prices of certain materials used in our and our customers&#146; businesses, including as a result
of the imposition of tariffs, governmental regulations affecting the sourcing of certain materials and equipment and other changes in U.S. trade relationships with other countries; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">cancellation provisions within our contracts and the risk that contracts expire and are not renewed or are
replaced on less favorable terms; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">loss of customers with whom we have long-standing or significant relationships; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the potential that participation in joint ventures or similar structures exposes us to liability and/or harm to
our reputation for acts or omissions by our partners; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">our inability or failure to comply with the terms of our contracts, which may result in additional costs,
unexcused delays, warranty claims, failure to meet performance guarantees, damages or contract terminations; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the inability or refusal of our customers or third-party contractors to pay for services, which could be
attributable to, among other things, the <FONT STYLE="white-space:nowrap">COVID-19</FONT> pandemic or the recent decrease in commodity prices and which could include the failure to collect our outstanding receivables, failure to recover amounts
billed to customers in bankruptcy, or failure to recover on change orders or contract claims; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">budgetary or other constraints that may reduce or eliminate tax incentives or government funding for projects,
which may result in project delays or cancellations; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">our ability to successfully complete our remaining performance obligations or realize our backlog;
</P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">risks associated with operating in international markets, including instability of foreign governments, currency
exchange fluctuations, and compliance with unfamiliar foreign legal systems and cultural </P></TD></TR></TABLE>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">5 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">

<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="9%">&nbsp;</TD>
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">
practices, the U.S. Foreign Corrupt Practices Act and other applicable anti-bribery and anti-corruption laws, and complex U.S. and foreign tax regulations and international treaties;
</P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">our ability to successfully identify, complete, integrate and realize synergies from acquisitions, including the
ability to retain key personnel from acquired businesses; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the potential adverse impact resulting from uncertainty surrounding acquisitions and investments, including the
potential increase in risks already existing in our operations and poor performance or decline in value of our investments; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the adverse impact of impairments of goodwill, other intangible assets, receivables, long-lived assets or
investments; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">our growth outpacing our decentralized management and infrastructure; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">inability to enforce our intellectual property rights or the obsolescence of such rights; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the impact of our unionized workforce on our operations, including labor stoppages or interruptions due to
strikes or lockouts; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the ability to access sufficient funding to finance desired growth and operations, including our ability to
access capital markets on favorable terms, as well as fluctuations in the price and volume of our common stock, debt covenant compliance, interest rate fluctuations and other factors affecting our financing and investing activities;
</P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">our ability to obtain performance bonds and other project security; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">our ability to meet the regulatory requirements applicable to us and our subsidiaries, including the
Sarbanes-Oxley Act of 2002 and the U.S. Investment Advisers Act of 1940; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">rapid technological and other structural changes that could reduce the demand for our services;
</P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">risks related to the implementation of new information technology systems; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">new or changed tax laws, treaties or regulations; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">our ability to realize deferred tax assets; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">legislative or regulatory changes that result in increased costs, including with respect of labor and healthcare
costs; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">significant fluctuations in foreign currency exchange rates; and </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the other risks and uncertainties described elsewhere herein and in Item 1A. Risk Factors of Part I of our Annual
Report on Form <FONT STYLE="white-space:nowrap">10-K</FONT> for the fiscal year ended December&nbsp;31, 2019, our Quarterly Report on Form <FONT STYLE="white-space:nowrap">10-Q</FONT> for the quarterly period ended March&nbsp;31, 2020, our Quarterly
Report on Form <FONT STYLE="white-space:nowrap">10-Q</FONT> for the quarterly period ended June&nbsp;30, 2020 and as may be detailed from time to time in our other public filings with the Securities and Exchange Commission. </P></TD></TR></TABLE>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">All of our forward-looking statements, whether written or oral, are expressly qualified by these cautionary statements and any other
cautionary statements that may accompany such forward-looking statements or that are otherwise included in or incorporated by reference in this prospectus. Although forward-looking statements reflect our good faith beliefs at the time made, reliance
should not be placed on forward-looking statements because they involve known and unknown risks, uncertainties and other factors, which may cause our actual results, performance or achievements to differ materially from anticipated future results,
performance or achievements expressed or implied by such forward-looking statements. In addition, we do not undertake and expressly disclaim any obligation to update or revise any forward-looking statements to reflect events or circumstances after
the date of this prospectus or otherwise. </P>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">6 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center"><B><A NAME="toc326517_5"></A>USE OF PROCEEDS </B></P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Unless we inform you otherwise in a prospectus supplement, we anticipate using any net proceeds from the sale of our securities offered by
this prospectus for general corporate purposes. These purposes may include, but are not limited to: </P> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">working capital; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">capital expenditures; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>

<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">acquisitions; and </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the repayment, refinancing, redemption or repurchase of indebtedness or other securities. </P></TD></TR></TABLE>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Pending any specific application, we may initially invest funds in short-term investments or apply them to the reduction of short-term
indebtedness or indebtedness under the credit agreement for our senior secured credit facility. </P>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">7 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center"><B><A NAME="toc326517_6"></A>DESCRIPTION OF CAPITAL STOCK </B></P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The following describes Quanta&#146;s common stock, preferred stock, restated certificate of incorporation (the &#147;certificate of
incorporation&#148;) and amended and restated bylaws (the &#147;bylaws&#148;). This description is a summary only and does not purport to be complete. We encourage you to read the complete text of our certificate of incorporation and bylaws, which
we have filed or incorporated by reference as exhibits to the registration statement of which this prospectus is a part. References to &#147;stockholders&#148; in this section refer to holders of our common stock, unless the context otherwise
requires. </P> <P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B>General </B></P> <P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Under our
certificate of incorporation, we have the authority to issue 610,000,000 shares of capital stock, consisting of 600,000,000 shares of common stock, par value $0.00001 per share (&#147;common stock&#148;), and 10,000,000 shares of preferred stock,
par value $0.00001 per share (&#147;preferred stock&#148;). </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">As of September&nbsp;4, 2020, there were 138,843,346 shares of our common
stock and no shares of our preferred stock issued and outstanding. All of the outstanding shares of our common stock are fully paid and nonassessable. </P>
<P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B><I>Voting Rights </I></B></P> <P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Our stockholders
are entitled to one vote for each share of common stock held on all matters voted upon by stockholders, including the election of directors. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Under our bylaws, when a quorum is present at any meeting of our stockholders, the affirmative vote of a majority of the votes cast
affirmatively or negatively on a matter will be the act of the stockholders, unless the question is one upon which by express provision of law, our certificate of incorporation, or our bylaws, a different vote is required or unless under the rules
and regulations of any stock exchange applicable to us or pursuant to any regulation applicable to us or our securities, a different vote is provided, in which case such express provision will govern and control the decision of such question. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Under our bylaws, in connection with an election of directors, each nominee for election in an uncontested election is elected by the vote of
the majority of votes cast with respect to such director at any meeting of our stockholders at which a quorum is present, meaning that the number of shares voted for such director must exceed the number of shares voted against such director;
provided, however, that in all elections other than uncontested elections, directors will be elected by a plurality of the votes cast at any meeting of the stockholders. If directors are to be elected by a plurality of the votes cast, stockholders
will not be permitted to vote against a nominee. Holders of our common stock have no right to cumulate their votes in an election of directors. </P>
<P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B><I>Dividend Rights </I></B></P> <P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Subject to the
preferred rights of the holders of shares of any class or series of our preferred stock, holders of our common stock are entitled to receive out of our funds legally available therefor, such dividends (payable in cash, stock or otherwise) as
Quanta&#146;s board of directors (the &#147;board of directors&#148;) may from time to time determine, payable to stockholders of record on such dates. The declaration and amount of future dividends is at the discretion of our board of directors and
will depend on, among other factors, our financial condition, results of operations, cash flows, current and anticipated expansion plans, requirements under Delaware law and other factors that our board of directors may deem relevant. </P>
<P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B><I>Liquidation Rights </I></B></P> <P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Our
stockholders are entitled to share equally and ratably in our net assets upon a liquidation or dissolution after the payment or provision for all liabilities, subject to any preferential liquidation rights of any preferred stock that at the time may
be outstanding. </P>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">8 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B><I>No Preemptive, Conversion or Redemption Rights </I></B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Our stockholders have no preemptive, subscription, conversion or redemption rights, and are not subject to further calls or assessments by us.
There are no sinking fund provisions applicable to our common stock. </P> <P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B><I>Listing </I></B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Our common stock is traded on the New York Stock Exchange under the symbol &#147;PWR.&#148; </P>
<P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B><I>Issuance of Preferred Stock </I></B></P> <P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Our
certificate of incorporation authorizes up to 10,000,000 shares of preferred stock. Preferred stock may be issued in one or more series as may be determined from time to time by the board of directors, and the board of directors, without further
approval of the stockholders, is authorized to fix by resolution or resolutions providing for the issue of each such series the voting powers, designations, preferences, and relative, participating, optional, redemption, conversion, exchange or
other special rights, qualifications, limitations or restrictions of such series, and the number of shares in each series, to the fullest extent permitted by law. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The prospectus supplement relating to any series of preferred stock Quanta offers will include specific terms relating to the offering and the
name of any transfer agent for that series. We will file the form of the preferred stock with the Securities and Exchange Commission before Quanta issues any preferred stock, and you should read any such form of preferred stock for provisions that
may be important to you. The prospectus supplement will include some or all of the following terms: </P> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the title of the preferred stock; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the maximum number of shares of the series; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the dividend rate or the method of calculating the dividend, the date from which dividends will accrue and
whether dividends will be cumulative or <FONT STYLE="white-space:nowrap">non-cumulative;</FONT> </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">any terms for the conversion or exchange of the preferred stock for other securities of Quanta or any other
entity; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">any redemption provisions; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">any liquidation preference; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">any voting rights; and </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">any other preferences and relative, participating, optional or other special rights or any qualifications,
limitations or restrictions on the rights of the shares. </P></TD></TR></TABLE> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">As described under &#147;Description of Depositary
Shares&#148; below, we may elect to offer depositary shares of preferred stock represented by depositary receipts. If we so elect, a depositary share may represent a fractional interest, to be specified in any applicable prospectus supplement, in a
share of preferred stock. If we issue depositary shares representing interests in preferred stock, those shares of preferred stock will be deposited with a depositary. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The purpose of authorizing the board of directors to determine these rights, preferences, privileges and restrictions is to eliminate delays
associated with a stockholder vote on specific issuances. The issuance of preferred stock, while providing flexibility in connection with possible acquisitions and other corporate purposes, could, among other things, adversely affect the voting
power of our then-existing stockholders, as well as dividend and liquidation payments on both common and preferred stock, and, under certain circumstances, make it more difficult for a third party to gain control of Quanta. </P>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">9 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B>Effects of Certain Provisions of Our Certificate of Incorporation and Bylaws and Delaware Law </B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Our certificate of incorporation, our bylaws and Delaware law contain provisions that may deter or render more difficult proposals to acquire
control of Quanta, including proposals a stockholder might consider to be in his or her best interest, impede or delay a change in membership of the board of directors and make removal of our management more difficult. </P>
<P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B><I>Action by Stockholders Without a Meeting </I></B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Our certificate of incorporation provides that any action to be taken by our stockholders must be effected at an annual or special meeting and
may not be effected by any consent in writing of such stockholders. </P> <P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B><I>Special Meetings of Stockholders </I></B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Our certificate of incorporation and bylaws provide that special meetings of stockholders may be called at any time only by the chairman of the
board of directors and shall be called within ten days after receipt of the written request of the board of directors, pursuant to a resolution of a majority of the board of directors to call a special meeting. Holders of our common stock do not
have the right to call a special meeting of stockholders. The business transacted at a special meeting of stockholders is confined to the purpose stated in the notice of the meeting. </P>
<P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B><I>Advance Notice Provisions </I></B></P> <P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Our
bylaws provide that proposals and director nominations made by a stockholder to be voted upon at any annual meeting or special meeting of the stockholders may be considered only if such proposal or director nomination is properly brought before such
meeting. In order for any matter, to be considered properly brought before such meeting, a stockholder must comply with certain requirements regarding advance notice to us. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Generally, in the case of an annual meeting, stockholders must deliver to the Secretary of Quanta a written notice between 90 and 120 days
before the anniversary date of our immediately preceding annual meeting of the stockholders. In the case of an annual meeting that is more than 30 days before or more than 30 days after such anniversary date, or in the event that no annual meeting
was held in the preceding year, stockholders must deliver such notice between 90 and 120 days prior to such annual meeting or within 10 days following the day on which public announcement of the date of such meeting is first made by us. In no event
will the adjournment of an annual meeting, or postponement of an annual meeting for which notice was given, or the public announcement of such adjournment or postponement, commence a new time period for any stockholder to give notice. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">To be in proper form, the notice must include, among other things, the name and address of the stockholder, certain information regarding the
shares owned by the stockholder, a brief description of the business desired to be brought by the stockholder at the meeting, the text of the proposal or business, the reasons for conducting such business at the meeting and any material interest in
such business of the stockholder and the beneficial owner, if any, on whose behalf the proposal is made. To nominate directors, the notice must include, as to each person whom the stockholder proposes to nominate for election or <FONT
STYLE="white-space:nowrap">re-election</FONT> as a director, all information relating to such person that would be required to be disclosed in solicitations of proxies for election of directors in an election contest, or is otherwise required, in
each case pursuant to Regulation 14A under the Exchange Act, as well as representations regarding whether a director nominee is a party to any agreement with respect to voting or compensation or that might limit such director nominee&#146;s exercise
of fiduciary duties, among other things. Additionally, the notice must include such other information about the stockholder, each proposal and nominee as required by the Securities and Exchange Commission. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Director nominations and stockholder proposals that are late or that do not include all required information may be rejected. This could
prevent stockholders from bringing certain matters before a meeting, including making nominations for directors. </P>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">10 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B><I>Vacancies on the Board of Directors </I></B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Our bylaws provide that, subject to the rights of the holders of any outstanding series of preferred stock and unless otherwise required by law
or resolution of our board of directors, vacancies on the board of directors arising through death, resignation, retirement, disqualification or removal, an increase in the number of directors or otherwise may be filled by a majority of the
directors then in office, though less than a quorum, or a successor or successors may be chosen at a special meeting of the stockholders called for that purpose. </P>
<P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B><I>Delaware Business Combination Statute </I></B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">We are a Delaware corporation and are subject to Section&nbsp;203 of the General Corporation Law of the State of Delaware (the
&#147;DGCL&#148;). Section&nbsp;203 of the DGCL prohibits a &#147;business combination&#148; between a corporation and an &#147;interested stockholder&#148; within three years of the time the stockholder became an interested stockholder, unless:
</P> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">prior to such time, the board of directors of the corporation approved either the business combination or the
transaction that resulted in the stockholder becoming an interested stockholder; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">upon consummation of the transaction that resulted in the stockholder becoming an interested stockholder, the
interested stockholder owned at least 85% of the voting stock of the corporation outstanding at the time the transaction commenced, exclusive of shares owned by directors who are also officers and by certain employee stock plans; or
</P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">at or subsequent to such time, the business combination is approved by the board of directors and authorized at a
stockholders&#146; meeting by at least <FONT STYLE="white-space:nowrap">two-thirds</FONT> of the outstanding voting stock that is not owned by the interested stockholder. </P></TD></TR></TABLE>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Generally, a &#147;business combination&#148; includes a merger, asset or stock sale, or other transaction resulting in a financial benefit to
the interested stockholder. Generally, an &#147;interested stockholder&#148; is a person who owns, individually or with or through other persons, 15% or more of the corporation&#146;s outstanding voting stock. </P>
<P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B><I>Forum Selection </I></B></P> <P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Our bylaws
provide that, unless we consent in writing to the selection of an alternative forum, and to the fullest extent permitted by law, the sole and exclusive forum for certain legal matters will be the Court of Chancery in the State of Delaware (or, if
the Court of Chancery does not have jurisdiction, the federal district court for the District of Delaware). This provision applies to (i)&nbsp;any derivative action or proceeding brought on behalf of Quanta, (ii)&nbsp;any action asserting a claim of
breach of a fiduciary duty owed by any of our present or former directors, officers or employees to Quanta or our stockholders, (iii)&nbsp;any action asserting a claim arising pursuant to any provision of the DGCL, (iv)&nbsp;any action asserting a
claim arising pursuant to any provision of the certificate of incorporation or bylaws (as either may be amended from time to time), or (v)&nbsp;any action asserting a claim governed by the internal affairs doctrine. </P>
<P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B>Transfer Agent and Registrar </B></P> <P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The
transfer agent and registrar for our common stock is American Stock Transfer&nbsp;&amp; Trust Company, LLC. </P>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">11 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center"><B><A NAME="toc326517_7"></A>DESCRIPTION OF DEBT SECURITIES </B></P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The debt securities that we may offer by this prospectus consist of unsecured notes, debentures or other evidences of indebtedness of the
Company (collectively, the &#147;debt securities&#148;). The following description of the terms of the debt securities sets forth certain general terms and provisions of the debt securities to which any prospectus supplement may relate. The
particular terms of the debt securities offered by any prospectus supplement and the extent, if any, to which such general provisions may apply to the debt securities so offered will be described in the prospectus supplement or other offering
material relating to such debt securities. Accordingly, for a description of the terms of a particular issue of debt securities, reference must be made to the prospectus supplement and such other offering material relating thereto and to the
following description. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The debt securities will be general obligations of the Company and will be senior debt of the Company. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Debt securities will be issued under an indenture (the &#147;Indenture&#148;) between the Company and U.S. Bank National Association or any
separate trustee appointed by the Company with respect to one or more series of debt securities (the &#147;Trustee&#148;). The following discussion of certain provisions of the Indenture is a summary only and does not purport to be a complete
description of the terms and provisions of the Indenture. The following discussion is qualified in its entirety by reference to the provisions of the Indenture. The Indenture is subject to any amendments or supplements that we may enter into from
time to time, as permitted under the Indenture. Except as otherwise defined in this prospectus, capitalized terms used in this prospectus have the meanings given to them in the Indenture. For additional information, you should review the Indenture
that is incorporated by reference as an exhibit to the registration statement of which this prospectus forms a part. We urge you to read the Indenture because it, and not the summary below, defines your rights as a holder of debt securities. </P>
<P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B>General </B></P> <P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The Indenture does not limit the
aggregate principal amount of debt securities that can be issued thereunder. The debt securities may be issued in one or more series as may be authorized from time to time by the Company&#146;s board of directors or established in one or more
supplemental indentures. You should read the prospectus supplement and any other offering material relating to a particular series of debt securities for any or all of the following terms of such series of debt securities offered by that prospectus
supplement and this prospectus: </P> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the title of the debt securities of the series; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">any limit on the aggregate principal amount of the debt securities of the series that may be authenticated and
delivered under the Indenture; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the date or dates on which the principal and premium, if any, with respect to the debt securities of the series
are payable or the method of determination thereof; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the rate or rates (which may be fixed or variable) at which the debt securities of the series shall bear interest
(if any) or the method of determining such rate or rates, the date or dates from which such interest shall accrue, the dates on which such interest shall be payable or the method by which such dates will be determined, the record dates for the
determination of holders thereof to whom such interest is payable (in the case of any debt securities registered as to principal and interest), and the basis upon which interest will be calculated if other than that of a <FONT
STYLE="white-space:nowrap">360-day</FONT> year of twelve <FONT STYLE="white-space:nowrap">30-day</FONT> months; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the place or places, if any, in addition to or instead of a corporate trust office of the Trustee where the
principal, premium, if any, and interest with respect to debt securities of the series shall be payable; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the price or prices at which, the period or periods within which and the terms and conditions upon which debt
securities of the series may be redeemed, in whole or in part, at the option of the Company or otherwise; </P></TD></TR></TABLE>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">12 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">

<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the obligation, if any, of the Company to redeem, purchase or repay debt securities of the series pursuant to any
sinking fund or analogous provisions or at the option of a holder thereof and the price or prices at which, the period or periods within which and the terms and conditions upon which debt securities of the series shall be redeemed, purchased or
repaid, in whole or in part, pursuant to such obligations; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">whether the debt securities will be convertible into or exchangeable for any other securities of the Company or
any other obligor and the applicable terms and conditions; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">if other than denominations of $2,000 and any integral multiple of $1,000 in excess thereof, the denominations in
which debt securities of the series shall be issuable; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">if the amount of principal, premium, if any, or interest with respect to the debt securities of the series may be
determined with reference to an index or pursuant to a formula, the manner in which such amounts will be determined; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">if the principal amount payable at the stated maturity of the debt securities of the series will not be
determinable as of any one or more dates prior to such stated maturity, the amount that will be deemed to be such principal amount as of any such date for any purpose, including the principal amount thereof which will be due and payable upon any
maturity other than the stated maturity or which will be deemed to be outstanding as of any such date (or, in any such case, the manner in which such deemed principal amount is to be determined), and, if necessary, the manner of determining the
equivalent thereof in United States currency; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">any changes or additions relating to the discharge, defeasance and covenant defeasance described below under the
heading &#147;&#151;Satisfaction and Discharge of the Indenture; Defeasance;&#148; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">if other than the coin or currency of the United States, the coin, currency, currencies or units of currencies in
which payment of the principal, premium, if any, and interest with respect to the debt securities of the series will be payable; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">if other than the principal amount, the portion of the principal amount of the debt securities of the series that
will be payable upon declaration of acceleration of maturity or provable in bankruptcy; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the terms, if any, of the transfer, mortgage, pledge or assignment as security for the debt securities of the
series of any properties, assets, moneys, proceeds, securities or other collateral; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">any addition to or change in the Events of Default (as defined below) with respect to the debt securities of the
series and any change in the right of the Trustee or the holders to declare the principal of and interest on such debt securities due and payable; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the terms, if any, of any guarantee of the payment of principal of and interest on the debt securities of the
series; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the applicability of, and any changes in or additions to, the covenants and definitions set forth in the
Indenture or the terms of the Indenture relating to consolidation, merger, sale, conveyance, transfer or lease described below under the heading &#147;&#151;Consolidation, Merger and Sale of Assets;&#148; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the identity of any trustees, authenticating or paying agents, transfer agents or registrars other than the
Trustee; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">if the debt securities of the series shall be issued in whole or in part in the form of a Global Security (as
defined below), the terms and conditions, if any, upon which such Global Security may be exchanged in whole or in part for other individual debt securities in definitive registered form and the Depositary (as defined below) for such Global Security;
</P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">with regard to debt securities of the series that do not bear interest, the dates for certain required reports to
the Trustee; and </P></TD></TR></TABLE>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">13 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">

<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">any other terms of the debt securities of the series which are not prohibited by the provisions of the Indenture
or applicable law. </P></TD></TR></TABLE> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The prospectus supplement will also describe any material U.S. federal income tax consequences or
other special considerations applicable to the series of debt securities to which such prospectus supplement relates, including those applicable to (1)&nbsp;debt securities with respect to which payments of principal, premium, if any, or interest
are determined with reference to an index or formula (including changes in prices of particular securities, currencies or commodities), (2) debt securities with respect to which principal, premium, if any, or interest is payable in a foreign or
composite currency, (3)&nbsp;debt securities that are issued at a discount below their stated principal amount, bearing no interest or interest at a rate that at the time of issuance is below market rates and (4)&nbsp;variable rate debt securities
that are exchangeable for fixed rate debt securities. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Payments of interest on debt securities may be made (1)&nbsp;at the office of the
Trustee at which its corporate trust office for such purpose is administered in the United States (the &#147;corporate office of the Trustee&#148;); (2) at the office of the Company&#146;s agent in New York City at which its corporate agency
business is conducted; (3)&nbsp;at the option of the Company, by check mailed to the registered holders thereof; or (4)&nbsp;if so provided in the applicable prospectus supplement, at the option of a holder by wire transfer to an account designated
by such holder. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Unless otherwise provided in the applicable prospectus supplement, if a payment date is not a business day, payment shall
be made on the next succeeding day that is a business day, and no interest shall accrue on any amount that would have been otherwise payable on such payment date if it were a business day for the intervening period. If a regular record date is not a
business day, the record date shall not be affected. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Unless otherwise provided in the applicable prospectus supplement, debt securities
may be transferred or exchanged at a corporate office of the Trustee, subject to the limitations provided in the Indenture, without the payment of any service charge, other than any tax or governmental charge payable in connection therewith. The
transferor of any debt security shall provide or cause to be provided to the Trustee all information necessary to allow the Trustee to comply with any applicable tax reporting obligations, including without limitation, any cost basis reporting
obligations under Internal Revenue Code Section&nbsp;6045. The Trustee may rely on information provided to it and shall have no responsibility to verify or ensure the accuracy of such information. </P>
<P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B>Registered Global Securities </B></P> <P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The debt
securities of a series may be issued in whole or in part in the form of one or more fully registered global securities (a &#147;Global Security&#148;) that will be deposited with The Depository Trust Company or a custodian or a nominee for a
depositary identified in the prospectus supplement relating to such series (the &#147;Depositary&#148;). In such case, one or more Global Securities will be issued in a denomination or aggregate denomination equal to the portion of the aggregate
principal amount of outstanding registered debt securities of the series to be represented by such Global Security or Securities. Unless and until it is exchanged in whole or in part for debt securities in definitive registered form, a Global
Security may not be registered for transfer or exchange except (1)&nbsp;by the Depositary to a nominee of such Depositary, (2)&nbsp;by a nominee of such Depositary to such Depositary or another nominee of such Depositary, (3)&nbsp;by such Depositary
or any such nominee to a successor of such Depositary or a nominee of such successor or (4)&nbsp;in any other circumstance described in an applicable prospectus supplement. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The specific terms of the depositary arrangement with respect to any portion of a series of debt securities to be represented by a Global
Security will be described in the prospectus supplement relating to such series. The Company anticipates that the following provisions will apply to all depositary arrangements. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Upon the issuance of a Global Security, the Depositary for such Global Security will credit, on its book-entry registration and transfer
system, the respective principal amounts of the debt securities represented by such Global Security to the accounts of persons that have accounts with such Depositary (&#147;participants&#148;). The accounts to be credited will be designated by any
dealers, underwriters or agents participating in the distribution </P>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">14 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman">
of such debt securities or by the Company if such debt securities are offered and sold directly by the Company. Ownership of beneficial interests in a Global Security will be limited to
participants or persons that may hold interests through participants. Ownership of beneficial interests in such Global Security will be shown on, and the transfer of that ownership will be effected only through, records maintained by the Depositary
for such Global Security (with respect to interests of participants) or by participants or persons that hold interests through participants (with respect to interests of persons other than participants). The laws of some states require that certain
purchasers of securities take physical delivery of such securities in definitive form. Such limits and such laws may impair the ability to transfer beneficial interests in a Global Security. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">So long as the Depositary for a Global Security, or its nominee, is the registered owner of such Global Security, such Depositary or such
nominee, as the case may be, will be considered the sole owner or holder of the debt securities represented by such Global Security for all purposes under the Indenture and the debt securities. Any notices required to be given to the holders while
the debt securities are Global Securities shall be given only to the Depositary. Except as set forth below, owners of beneficial interests in a Global Security will not (1)&nbsp;be entitled to have the debt securities represented by such Global
Security registered in their names, (2)&nbsp;receive or be entitled to receive physical delivery of such debt securities in definitive form and (3)&nbsp;be considered the owners or holders thereof under the Indenture. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Principal, premium, if any, and interest payments on debt securities represented by a Global Security registered in the name of a Depositary
or its nominee will be made to such Depositary or its nominee, as the case may be, as the registered owner of such Global Security. None of the Company, the Trustee, any registrar, any paying agent or any agent of the Company or the Trustee will
have any responsibility or liability for (1)&nbsp;any aspect of the records relating to or payments made on account of beneficial ownership interests in such Global Security or for maintaining, supervising or reviewing any records relating to such
beneficial ownership interests, (2)&nbsp;the payments to the beneficial owners of such Global Security of amounts paid to such Depositary or its nominee or (3)&nbsp;any other matter relating to the actions and practices of such Depositary, its
nominees or any of its direct or indirect participants. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The Company expects that the Depositary for any debt securities represented by a
Global Security, upon receipt of any payment of principal, premium, if any, or interest, will credit, in accordance with the Depositary&#146;s policies, participants&#146; accounts with payments in amounts proportionate to their respective
beneficial interests in the principal amount of such Global Security as shown on the records of such Depositary. The Company also expects that payments by participants to owners of beneficial interests in such Global Security held through such
participants will be governed by standing instructions and customary practices, as is now the case with the securities held for the accounts of customers registered in &#147;street names&#148; and will be the responsibility of such participants, and
will not be the responsibility of the Company. The Company will not be liable for any delay by the Depositary or any of its participants in identifying the beneficial owners of any Global Security, and the Company may conclusively rely on and will
be protected in relying on instructions from the Depositary or its nominee for all purposes. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">If the Depositary for any debt securities
represented by a Global Security is at any time unwilling, unable, ineligible or unqualified under applicable law to continue as Depositary and a successor Depositary is not appointed by the Company within 90 days, the Company will issue such debt
securities in definitive form in exchange for such Global Security. In addition, the Company may at any time and in its sole discretion determine not to have any of the debt securities of a series represented by one or more Global Securities and, in
such event, will issue debt securities of such series in definitive form in exchange for all of the Global Security or Global Securities representing such debt securities. In the event that the Company issues debt securities in definitive form in
exchange for such Global Securities, ownership of beneficial interests in such debt securities will be shown on, and the transfer of that ownership will be effected only through, records maintained by (or on behalf of) the Company for such debt
securities. In connection with any proposed exchange of a debt security in definitive form for a Global Security, there shall be provided to the Trustee all information necessary to allow the Trustee to comply with any applicable tax reporting
obligations, including without limitation, any cost basis reporting obligations under Internal Revenue Code Section&nbsp;6045. The Trustee may rely on information provided to it and shall have no responsibility to verify or ensure the accuracy of
such information. </P>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">15 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B>Certain Covenants </B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The Indenture contains certain covenants of the Company, including the following: </P>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the Company will punctually pay or cause to be paid the principal of, and premium, if any, and interest on, the
debt securities, at the places and times and in the manner provided in the Indenture and in the debt securities; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the Company will maintain an office or agency where the debt securities may be presented or surrendered for
payment, transfer or exchange and where notices and demands to or upon the Company in respect of the debt securities and the Indenture may be served; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the Company will deliver to the Trustee, on or before a date not more than four months after the end of each
fiscal year of the Company, a statement complying with the Trust Indenture Act signed by an Officer of the Company, which need not constitute an Officers&#146; Certificate, stating (1)&nbsp;that a review of the activities of the Company during such
year and of the Company&#146;s performance under the Indenture and under the terms of the debt securities has been made under his or her supervision, (2)&nbsp;whether or not, to the best of his or her knowledge, the Company was in compliance with
all conditions and covenants under the Indenture during such year and (3)&nbsp;if, to the best of his knowledge, the Company is in Default, specifying all such Defaults known to such Officer and the nature and status thereof; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the Company will, upon request of the Trustee, execute and deliver such further instruments and do such further
acts as may reasonably be necessary or proper to carry out more effectually the purposes of the Indenture; and </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the Company will do or cause to be done all things necessary to preserve and keep in full force and effect its
existence. </P></TD></TR></TABLE> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Any restrictive covenants of the Company applicable to any series of debt securities will be described in
the applicable prospectus supplement or other offering material. </P> <P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B>Events of Default and Remedies </B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The following events are defined in the Indenture as &#147;Events of Default&#148; with respect to a series of debt securities: </P>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">default in the payment of any installment of interest on any debt securities of that series as and when the same
become due and payable and continuance of such default for a period of 30 days; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">default in the payment of principal or premium, if any, with respect to any debt securities of that series as and
when the same become due and payable, whether at maturity, upon redemption, by declaration, upon required purchase or otherwise; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">default in the payment of any sinking fund payment with respect to any debt securities of that series as and when
the same become due and payable and continuance of such default for a period of 30 days; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">failure on the part of the Company to comply with any of the covenants or agreements on the part of the Company
in the debt securities of that series, in any resolution of the board of directors of the Company authorizing the issuance of that series of debt securities, in the Indenture with respect to such series or in any supplemental indenture with respect
to such series (other than a covenant a default in the performance of which is otherwise specifically dealt with) continuing for a period of 90 days after the date on which written notice specifying such failure and requiring the Company to remedy
the same has been given, by registered or certified mail or by overnight courier guaranteeing next day delivery, to the Company by the Trustee or to the Company and the Trustee by the holders of at least 25% in aggregate principal amount of the debt
securities of that series at the time outstanding; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the Company (1)&nbsp;voluntarily commences any proceeding or files any petition seeking relief under the United
States Bankruptcy Code or other federal or state bankruptcy, insolvency or similar law, (2)&nbsp;consents to the institution of, or fails to controvert within the time and in the manner prescribed by law, any such proceeding or the filing of any
such petition, (3)&nbsp;applies for or consents to the appointment of a receiver, trustee, custodian, sequestrator or similar official for the Company or for a </P></TD></TR></TABLE>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">16 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">

<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="9%">&nbsp;</TD>
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">
substantial part of its property, (4)&nbsp;files an answer admitting the material allegations of a petition filed against it in any such proceeding, (5)&nbsp;makes a general assignment for the
benefit of creditors, (6)&nbsp;admits in writing its inability to pay, or fails generally to pay, its debts as they become due or (7)&nbsp;takes any comparable action under any foreign laws relating to insolvency; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the entry of an order or decree by a court having competent jurisdiction for (1)&nbsp;relief with respect to the
Company or a substantial part of its property under the United States Bankruptcy Code or any other federal or state bankruptcy, insolvency or similar law, (2)&nbsp;the appointment of a receiver, trustee, custodian, sequestrator or similar official
for the Company or for a substantial part of its property or (3)&nbsp;the <FONT STYLE="white-space:nowrap">winding-up</FONT> or liquidation of the Company, and such order or decree continues unstayed and in effect for 90 consecutive days, or any
similar relief is granted under any foreign laws and the order or decree stays in effect for 90 consecutive days; and </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">any other Event of Default provided with respect to debt securities of that series. </P></TD></TR></TABLE>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">An Event of Default with respect to one series of debt securities may not necessarily be an Event of Default for another series and Events of
Default for any series of debt securities may be modified as described in the applicable prospectus supplement. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">If an Event of Default
described in the first, second, third, fourth or seventh bullet points above occurs and is continuing with respect to any series of outstanding debt securities, unless the principal and interest with respect to all the debt securities of such series
has already become due and payable, either the Trustee or the holders of not less than 25% in aggregate principal amount of the debt securities of such series then outstanding may declare the principal of (or, if original issue discount debt
securities, such portion of the principal amount as may be specified in such series) and interest on all the debt securities of such series due and payable immediately. If an Event of Default described in the fifth or sixth bullet points above
occurs, unless the principal and interest with respect to all the debt securities of the series has become due and payable, the principal of (or, if any series are original issue discount debt securities, such portion of the principal amount as may
be specified in such series) and interest on all debt securities of all series then outstanding will become and be immediately due and payable without any declaration or other act on the part of the Trustee or any holder of debt securities. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">If an Event of Default occurs and is continuing, the Trustee will be entitled and empowered to institute any action or proceeding for the
collection of the sums so due and unpaid or to enforce the performance of any provision of the debt securities of the affected series or the Indenture, to prosecute any such action or proceeding to judgment or final decree and to enforce any such
judgment or final decree against the Company or any other obligor on the debt securities of such series (and collect in the manner provided by law out of the property of the Company or any other obligor upon the debt securities of such series
wherever situated the moneys adjudged or decreed to be payable). In addition, if there are any pending proceedings for the bankruptcy or reorganization of the Company or any other obligor on the debt securities, or if a receiver, trustee or similar
official has been appointed for its property, the Trustee will be entitled and empowered, irrespective of whether the principal of any series of debt securities is due and payable, to file and prove a claim for the whole amount of principal,
premium, if any, and interest (or, in the case of original issue discount debt securities, such portion of the principal amount as may be specified in the terms of such series) owing and unpaid with respect to the debt securities. No holder of any
debt security of any series will have any right to institute any action or proceeding upon, under or with respect to the Indenture for the appointment of a receiver or trustee or for any other remedy, unless (1)&nbsp;such holder previously has given
to the Trustee written notice of an Event of Default with respect to debt securities of that series and of the continuance thereof, (2)&nbsp;the holders of not less than 25% in aggregate principal amount of the outstanding debt securities of that
series have made written request to the Trustee to institute such action or proceeding with respect to such Event of Default and have offered to the Trustee such security or indemnity as it may require against the costs, expenses, and liabilities to
be incurred therein or thereby and (3)&nbsp;the Trustee, for 60 days after its receipt of such notice, request and offer of security or indemnity, has failed to institute such action or proceeding and no direction inconsistent with such written
request has been given to the Trustee pursuant to the provisions of the Indenture. </P>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">17 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Prior to the acceleration of the maturity of the debt securities of any series, the holders
of a majority in aggregate principal amount of the debt securities of that series at the time outstanding may, on behalf of the holders of all debt securities of that series, waive any past default or Event of Default and its consequences for that
series, except (1)&nbsp;a default in the payment of the principal, premium, if any, or interest with respect to such debt securities or (2)&nbsp;a default with respect to a provision of the Indenture that cannot be amended without the consent of
each holder affected thereby. In the case of any such waiver, such default so waived will cease to exist, any Event of Default arising therefrom will be deemed to have been cured for all purposes and the Company, the Trustee and the holders of the
debt securities of that series will be restored to their former positions and rights under the Indenture. Following acceleration of the maturity of the debt securities of a series (including acceleration as specified in the fifth and sixth bullet
points), the holders of a majority in principal amount of such series may rescind an acceleration of the maturity of the series and its consequences if such rescission would not conflict with a rendered judgment or decree and all existing Events of
Default (except nonpayment of principal or interest solely due to such acceleration) have been cured or waived, and the Company has paid the Trustee its compensation and all sums paid or advanced by the Trustee hereunder and the reasonable and
documented <FONT STYLE="white-space:nowrap"><FONT STYLE="white-space:nowrap">out-of-pocket</FONT></FONT> compensation, expenses, disbursements and advances of the Trustee, its agents and counsel. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The Trustee shall have the right to decline to follow any direction of the holders of a majority in aggregate principal amount of the debt
securities of any series if the Trustee being advised by counsel determines that the action so directed may not lawfully be taken, or if the Trustee shall by a responsible officer or officers determine that the action so directed would involve it in
personal liability or would be unjustly prejudicial to the holders of the debt securities of such series not taking part in such direction. The Trustee shall be under no obligation to exercise any of the rights or powers vested in it under the
Indenture at the request, order or direction of any of the holders of debt securities of any series pursuant to the provisions of the Indenture, unless such holders shall have offered to the Trustee security or indemnity satisfactory to it against
the costs, expenses and liabilities which may be incurred therein or thereby. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The Trustee is required to give, within 90 days after the
occurrence of a default actually known to a responsible officer of the Trustee with respect to a series of debt securities, to the holders of the debt securities of such series notice of all defaults with respect to such series so known to it,
unless such defaults have been cured or waived before the giving of such notice; provided, however, that except in the case of default in the payment of principal, premium, if any, or interest with respect to the debt securities of such series or in
the making of any sinking fund or purchase fund payment with respect to the debt securities of such series, the Trustee will be protected in withholding such notice if it in good faith determines that the withholding of such notice is in the
interest of the holders of such debt securities. </P> <P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B>Modification of the Indenture </B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The Company and the Trustee may, from time to time, enter into supplemental indentures without the consent of the holders of debt securities
issued under the Indenture for one or more of the following purposes: </P> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">to evidence the succession of another person to the Company pursuant to the provisions of the Indenture and the
assumption by such successor of the covenants, agreements and obligations of the Company in the Indenture and in the debt securities; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">to surrender any right or power conferred upon the Company by the Indenture, to add to the covenants of the
Company such further covenants, restrictions, conditions or provisions for the protection of the holders of all or any series of debt securities as the board of directors of the Company shall consider to be for the protection of the holders of such
debt securities and to make the occurrence, or the occurrence and continuance, of a default in any of such additional covenants, restrictions, conditions or provisions a default or an Event of Default under the Indenture (provided, however, that
with respect to any such additional covenant, restriction, condition or provision, such supplemental indenture may provide for a period of grace after default, which may be shorter or longer than that allowed in the case of other defaults, may
provide for an immediate enforcement upon such default, may limit the remedies </P></TD></TR></TABLE>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">18 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">

<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="9%">&nbsp;</TD>
<TD VALIGN="top"> <P STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">
available to the Trustee upon such default or may limit the right of holders of a majority in aggregate principal amount of any or all series of debt securities to waive such default);
</P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">to cure any ambiguity or to correct or supplement any provision contained in the Indenture, in any supplemental
indenture or in any debt securities that may be defective or inconsistent with any other provision contained therein, to convey, transfer, assign, mortgage or pledge any property to or with the Trustee or to make such other provisions in regard to
matters or questions arising under the Indenture as do not adversely affect the interests in any material respect of any holders of debt securities of any series; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">to modify or amend the Indenture in such a manner as to permit the qualification of the Indenture or any
supplemental indenture under the Trust Indenture Act, as then in effect; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">to add or change any of the provisions of the Indenture that would change or eliminate any restrictions on the
payment of principal, premium, if any, or interest with respect to the debt securities so long as any such action does not adversely affect the interests of the holders of debt securities in any material respect or permit or facilitate the issuance
of debt securities of any series in uncertificated form; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">to evidence the succession of another corporation to the Company and the assumption by any such successor of the
covenants of the Company in the Indenture and in the debt securities; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">to add guarantees with respect to the debt securities or to secure the debt securities; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">to add to, change or eliminate any of the provisions of the Indenture with respect to one or more series of debt
securities, so long as any such addition, change or elimination not otherwise permitted under the Indenture (1)&nbsp;neither applies to any debt security of any series created prior to the execution of such supplemental indenture and entitled to the
benefit of such provision nor modifies the rights of the holders of any such debt security with respect to such provision or (2)&nbsp;becomes effective only when there is no such debt security outstanding; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">to evidence and provide for the acceptance of appointment by a successor or separate Trustee with respect to the
debt securities of one or more series and to add to or change any of the provisions of the Indenture as shall be necessary to provide for or facilitate the administration of the Indenture by more than one Trustee; and </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">to establish the form or terms of debt securities of any series, as described under the heading
&#147;&#151;General&#148; above. </P></TD></TR></TABLE> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">With the consent of the holders of a majority in aggregate principal amount of the
outstanding debt securities of each series affected thereby, the Company and the Trustee may from time to time and at any time enter into a supplemental indenture for the purpose of adding any provisions to, changing in any manner or eliminating any
of the provisions of the Indenture or of any supplemental indenture or modifying in any manner the rights of the holders of the debt securities of such series; provided, however, that without the consent of the holders of each Debt Security so
affected, no such supplemental indenture may (1)&nbsp;reduce the percentage in principal amount of debt securities of any series whose holders must consent to an amendment, (2)&nbsp;reduce the rate of or extend the time for payment of interest on
any debt security, (3)&nbsp;reduce the principal of or extend the stated maturity of any debt security, (4)&nbsp;reduce the premium, if any, payable upon the redemption of any debt security or change the time at which any debt security may or must
be redeemed, provided, however, that any amendment to the notice requirements may be made with the consent of the Holders of at least a majority in aggregate principal amount of the outstanding debt securities of such series, (5)&nbsp;make any debt
security payable in a currency other than that stated in the debt security, (6)&nbsp;release any security that may have been granted with respect to the debt securities or (7)&nbsp;make any change in certain provisions of the Indenture relating to
waivers of defaults or modifications of the Indenture by the consent of the holders of the debt securities. </P>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">19 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B>Consolidation, Merger and Sale of Assets </B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The Company may not consolidate with or merge with or into any person, or convey, transfer or lease all or substantially all of its assets,
unless the following conditions have been satisfied: </P> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">either (1)&nbsp;the Company is the continuing person in the case of a merger or (2)&nbsp;the resulting, surviving
or transferee person, if other than the Company (the &#147;Successor Company&#148;), is a corporation organized and existing under the laws of the United States, any State thereof or the District of Columbia and expressly assumes pursuant to a
supplemental indenture all of the obligations of the Company under the debt securities and the Indenture; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">immediately after giving effect to such transaction (and treating any indebtedness that becomes an obligation of
the Successor Company or any subsidiary of the Company as a result of such transaction as having been incurred by the Successor Company or such subsidiary at the time of such transaction), no default or Event of Default would occur or be continuing;
and </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the Company has delivered to the Trustee an officers&#146; certificate and an opinion of counsel (which opinion
of counsel may be subject to customary assumptions, qualifications and exclusions), each stating that such consolidation, merger, or transfer and such supplemental indenture (if any) comply with the Indenture. </P></TD></TR></TABLE>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">If the Successor Company expressly assumes all of the obligations of the Company under the debt securities and the Indenture, the Company will
promptly thereafter be released from such obligations. </P> <P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B>Satisfaction and Discharge of the Indenture; Defeasance </B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The Indenture will generally cease to be of any further effect with respect to a series of debt securities if (1)&nbsp;the Company has
delivered to the Trustee for cancellation all debt securities of such series (with certain limited exceptions) or (2)&nbsp;all debt securities of such series not theretofore delivered to the Trustee for cancellation have become due and payable, or
are by their terms to become due and payable within one year or are to be called for redemption within one year, and the Company has irrevocably deposited or caused to be deposited with the Trustee as trust funds the entire amount in the currency in
which the debt securities are denominated sufficient to pay at maturity or upon redemption all such debt securities (other than any debt securities which shall have been destroyed, lost or stolen and which shall have been replaced or paid),
including principal and premium, if any, and interest due or to become due on such date of maturity or redemption date, as the case may be, and if, in either case, the Company also pays or causes to be paid all other sums payable under the Indenture
by the Company, and the Company delivers to the Trustee an officers&#146; certificate and an opinion of counsel (which opinion of counsel may be subject to customary assumptions, qualifications and exclusions), each stating that all conditions
precedent to the discharge of the debt securities of such series as contemplated by the Indenture have been complied with. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">In addition,
the Company has a &#147;legal defeasance option&#148; (pursuant to which it may terminate, with respect to the debt securities of a particular series, all of its obligations under such debt securities and the Indenture with respect to such debt
securities) and a &#147;covenant defeasance option&#148; (pursuant to which it may terminate, with respect to the debt securities of a particular series, its obligations with respect to such debt securities under certain specified covenants
contained in the Indenture or supplemental indenture). If the Company exercises its legal defeasance option with respect to a series of debt securities, payment of such debt securities may not be accelerated because of an Event of Default. If the
Company exercises its covenant defeasance option with respect to a series of debt securities, payment of such debt securities may not be accelerated because of an Event of Default related to the specified covenants. </P>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">20 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The Company may exercise its legal defeasance option or its covenant defeasance option with
respect to the debt securities of a series only if: </P> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the Company irrevocably deposits or causes to be deposited in trust with the Trustee cash, U.S. Government
Obligations, or a combination thereof, for the payment of principal, premium, if any, and interest with respect to such series to maturity or redemption, as the case may be; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the Company delivers to the Trustee a certificate from a nationally recognized firm of independent accountants
expressing their opinion that the payments of principal and interest when due and without reinvestment on the deposited U.S. Government Obligations plus any deposited money without investment will provide cash at such times and in such amounts as
will be sufficient to pay the principal, premium, if any, and interest when due with respect to all the debt securities of such series to maturity or redemption, as the case may be; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">91 days pass after the deposit is made and during the <FONT STYLE="white-space:nowrap">91-day</FONT> period no
default described in the fifth or sixth bullet points under the heading &#147;&#151;Events of Default and Remedies&#148; above with respect to the Company occurs that is continuing at the end of such period; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">no default has occurred and is continuing on the date of such deposit and immediately after giving effect
thereto; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the Company delivers to the Trustee an opinion of counsel (which opinion of counsel may be subject to customary
assumptions, qualifications and exclusions) to the effect that the trust resulting from the deposit does not constitute, or is qualified as, a regulated investment company required to register under the Investment Company Act of 1940;
</P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the Company delivers to the Trustee an opinion of counsel (which opinion of counsel may be subject to customary
assumptions, qualifications and exclusions) addressing certain U.S. federal income tax matters relating to the defeasance; and </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the Company delivers to the Trustee an officers&#146; certificate and an opinion of counsel (which opinion of
counsel may be subject to customary assumptions, qualifications and exclusions), each stating that all conditions precedent to the defeasance and discharge of the debt securities of such series as contemplated by the Indenture have been complied
with. </P></TD></TR></TABLE> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The Trustee will hold in trust money or U.S. Government Obligations deposited with it as described above and will
apply the deposited money and the proceeds from deposited U.S. Government Obligations to the payment of principal, premium, if any, and interest with respect to the debt securities of the defeased series. </P>
<P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B>The Trustee </B></P> <P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The Indenture does not
prohibit the Trustee from serving as trustee under any other indenture to which the Company may be a party from time to time or from engaging in other transactions with the Company. The Company may maintain banking and other commercial relationships
with the Trustee and its affiliates in the ordinary course of business and the Trustee may own debt securities. The Trustee assumes no responsibility for the accuracy or completeness of the information concerning the Company or its affiliates or any
other party contained in this prospectus or the related documents or for any failure by us or any other party to disclose events that may have occurred and may affect the significance or accuracy of such information. The Trustee shall not be
responsible for monitoring the rating status of the Company or its affiliates, making any request upon any rating agency, or determining whether any rating event with respect to the debt securities of any series has occurred. The Trustee may resign
at any time with respect to all or any series of debt securities. The holders of a majority in aggregate principal amount of debt securities of a particular series may remove the Trustee for such series and appoint a successor Trustee. The Company
shall remove the Trustee for the causes set forth in the Indenture, including the Trustee&#146;s failure to satisfy applicable requirements under the Trust Indenture Act of 1939 or failure to maintain a combined capital and surplus of at least
$50,000,000. </P>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">21 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Except as otherwise provided with respect to removal by the holders of a series of debt
securities, in any of the foregoing events of resignation or removal of the Trustee, the Company shall appoint a successor Trustee and such appointment, and the retiring Trustee&#146;s resignation or removal, shall become effective upon acceptance
by the successor Trustee. </P> <P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B>Governing Law </B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The Indenture is, and the debt securities will be, governed by, and construed in accordance with, the laws of the State of New York. The
Indenture provides that the Company and the Trustee, and each holder of a debt security by its acceptance thereof, irrevocably waives, to the fullest extent permitted by applicable law, any and all right to trial by jury in any legal proceeding
arising out of or relating to the Indenture, the debt securities or any transaction contemplated thereby. </P>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">22 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center"><B><A NAME="toc326517_8"></A>DESCRIPTION OF WARRANTS </B></P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">We may issue warrants to purchase any combination of common stock, preferred stock, debt securities, depositary shares and purchase contracts.
Each warrant will entitle the holder to purchase for cash a number of securities at the exercise price as will in each case be described in, or can be determined from, the applicable prospectus supplement relating to the offered warrants. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Warrants may be issued independently or together with any securities and may be attached to or separate from the securities. The warrants will
be issued under warrant agreements to be entered into between us and a bank or trust company, as warrant agent. You should read the particular terms of the warrants, which will be described in more detail in any applicable prospectus supplement. The
particular terms of any warrants offered by any prospectus supplement, and the extent to which the general provisions summarized below may apply to the offered securities, will be described in a prospectus supplement. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Any applicable prospectus supplement will describe the terms of warrants we offer, the warrant agreement relating to the warrants and the
certificates representing the warrants, including, to the extent applicable: </P> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the title of the warrants; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the aggregate number of warrants; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the price or prices at which the warrants will be issued; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the currency or currencies, including composite currencies or currency units, in which the price of the warrants
may be payable if not payable in U.S. dollars; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the designation, number or aggregate principal amount and terms of the securities purchasable upon exercise of
the warrants, and the procedures and conditions relating to the exercise of the warrants; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the date on which the right to exercise the warrants will commence, and the date on which the right will expire;
</P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the designation and terms of any related securities with which the warrants are issued, and the number of the
warrants issued with each security; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the date, if any, on and after which the warrants and the related securities will be separately transferable;
</P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the maximum or minimum number of warrants that may be exercised at any time; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">if appropriate, a discussion of material United States federal income tax considerations; and
</P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">any other terms of the warrants. </P></TD></TR></TABLE>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">23 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center"><B><A NAME="toc326517_9"></A>DESCRIPTION OF DEPOSITARY SHARES </B></P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Shares of preferred stock may be offered either separately or represented by depositary shares. We may also, at our option, elect to offer
fractional shares of preferred stock. If we exercise this option, we will issue receipts for depositary shares, each of which will represent a fraction of a share of a particular series of preferred stock, to be described in an applicable prospectus
supplement. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The shares represented by depositary shares will be deposited under a deposit agreement between us and a bank or trust
company selected by us and having its principal office in the United States and having a combined capital and surplus of at least $50,000,000. Subject to the terms of the deposit agreement, each owner of a depositary share will be entitled, in
proportion to the applicable share or fraction thereof represented by the depositary share, to all of the rights and preferences, if any, of the share represented thereby, including any dividend, voting, redemption, conversion and liquidation
rights. The depositary shares will be evidenced by depositary receipts issued pursuant to the deposit agreement. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The particular terms of
the depositary shares offered by any prospectus supplement will be described in a prospectus supplement, which will also include a discussion of certain United States federal income tax consequences. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">We will include a copy of the form of deposit agreement, including the form of depositary receipt, and any other instrument establishing the
terms of any depositary shares we offer as exhibits to a filing we will make with the Securities and Exchange Commission in connection with that offering. See &#147;Where You Can Find More Information.&#148; </P>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">24 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center"><B><A NAME="toc326517_10"></A>DESCRIPTION OF PURCHASE CONTRACTS AND PURCHASE UNITS </B></P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">We may issue purchase contracts representing contracts obligating holders, subject to the terms of such purchase contracts, to purchase from
us, and us to sell to the holders, a specified or varying number of our common stock, preferred stock or other securities described in this prospectus at a future date or dates. Alternatively, the purchase contracts may, subject to the terms of such
purchase contracts, obligate us to purchase from holders, and obligate the holders to sell to us, a specified or varying number of common stock, preferred stock or other securities described in this prospectus. The price per unit of our common
stock, preferred stock or other securities described in this prospectus and number of units may be fixed at the time the purchase contracts are entered into or may be determined by reference to a specific formula set forth in the purchase contracts.
We may issue the purchase contracts separately or as part of units, which we refer to as &#147;purchase units,&#148; consisting of a purchase contract and other securities or obligations issued by us or third parties, including government
securities, in each case, securing the holders&#146; obligations to purchase the relevant securities under the purchase contracts. The purchase contracts may require us to make periodic payments to the holders of the purchase contracts or purchase
units or vice versa, and such payments may be unsecured or prefunded on some basis. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Any applicable prospectus supplement will describe
the terms of any purchase contract or purchase units. The description in a prospectus supplement will not necessarily be complete and will be qualified in its entirety by reference to the purchase contracts, and, if applicable, collateral
arrangements and depositary arrangements, relating to the purchase contracts or purchase units. </P>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">25 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center"><B><A NAME="toc326517_11"></A>DESCRIPTION OF UNITS </B></P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">We may issue units of securities consisting of one or more of the following securities: common stock, preferred stock, debt securities,
warrants, depositary shares and purchase contracts. We may evidence each series of units issued by unit certificates that we will issue under a separate unit agreement. We may enter into unit agreements with a unit agent. Each unit agent will be a
bank or trust company that we select. You should read the particular terms of these documents, which will be described in more detail in a prospectus supplement. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">If we offer any units, certain terms of that series of units will be described in a prospectus supplement, including, without limitation, the
following, as applicable: </P> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the title of the series of units; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">identification and description of the separate constituent securities comprising the units;
</P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the price or prices at which the units will be issued; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the date, if any, on and after which the constituent securities comprising the units will be separately
transferable; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">if appropriate, a discussion of material United States federal income tax considerations; and
</P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">any other terms of the units and their constituent securities. </P></TD></TR></TABLE>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">26 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center"><B><A NAME="toc326517_12"></A>PLAN OF DISTRIBUTION </B></P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">We may sell the securities on a delayed or continuous basis in and outside the United States through the methods described below or through
any other method permitted pursuant to applicable law, including through a combination of such methods. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">A prospectus supplement, if
required, will set forth any required information such as the terms of the offering and the method of distribution and will include the following information: </P> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the name or names of any underwriters or agents; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the purchase price of the securities from us; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">the net proceeds to us from the sale of the securities; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">any over-allotment options under which underwriters may purchase additional securities from us;
</P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">any underwriting discounts, commissions and other items constituting compensation to underwriters, dealers or
agents; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">any public offering price; </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">any discounts or concessions allowed or reallowed or paid to dealers; and </P></TD></TR></TABLE>
<P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">any securities exchange or market on which the securities offered in a prospectus supplement may be listed.
</P></TD></TR></TABLE> <P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B>Sale Through Underwriters or Dealers </B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">If we use underwriters in the sale of securities, the underwriters will acquire the securities for their own account. The underwriters may
resell the securities from time to time in one or more transactions, including negotiated transactions, at a fixed public offering price or at varying prices determined at the time of sale. Underwriters may offer securities to the public either
through underwriting syndicates represented by one or more managing underwriters or directly by one or more firms acting as underwriters. The obligations of the underwriters to purchase the securities may be subject to conditions, and the
underwriters will be obligated to purchase all the offered securities if they purchase any of them. The underwriters may change from time to time any initial public offering price and any discounts or concessions allowed or reallowed or paid to
dealers. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Underwriters may sell our common stock under this prospectus by any method permitted by law deemed to be an &#147;at the
market&#148; offering as defined in Rule 415 under the Securities Act, which includes sales made directly on the NYSE, on any other existing trading market for our common stock or to or through a market maker, or in privately negotiated
transactions. Unless stated otherwise in any applicable prospectus supplement, the sales agent with respect to any such at the market offering will make all sales using commercially reasonable efforts consistent with its normal trading and sales
practices, on mutually agreeable terms between the sales agent and us. Any applicable prospectus supplement will include the amount of any compensation to be received by the sales agent. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">During and after an offering through underwriters, the underwriters may purchase and sell the securities in the open market. These
transactions may include overallotment and stabilizing transactions and purchases to cover syndicate short positions created in connection with the offering. The underwriters also may impose a penalty bid, which means that selling concessions
allowed to syndicate members or other broker-dealers for the offered securities sold for their account may be reclaimed by the syndicate if the offered securities are repurchased by the syndicate in stabilizing or covering transactions. These
activities may stabilize, maintain or otherwise affect the market price of the offered securities, which may be higher than the price that might otherwise prevail in the open market. If commenced, the underwriters may discontinue these activities at
any time. </P>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">27 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">If we use dealers in the sale of securities, we will sell the securities to them as
principals. They may then resell those securities to the public at varying prices determined by the dealers at the time of resale. We also may agree to sell, and the relevant underwriters or agents may agree to solicit offers to purchase, blocks of
securities. The terms of each such agreement will be set forth in more detail in any applicable prospectus supplement and any related free writing prospectus. The dealers participating in any sale of the securities may be deemed to be underwriters
within the meaning of the Securities Act with respect to any sale of those securities. If required, we will include in any applicable prospectus supplement the names of the dealers and the terms of the transaction. </P>
<P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B>Direct Sales and Sales Through Agents </B></P> <P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">We
may sell the securities directly. In that event, no underwriters or agents would be involved. We also may sell the securities through agents we designate from time to time to solicit offers from purchasers to purchase the securities included in this
prospectus or to sell such securities in ordinary brokerage transactions on our behalf. If required, a prospectus supplement will name any agent involved in the offer or sale of the offered securities and will describe any commissions payable by us
to the agent. Unless stated otherwise in any applicable prospectus supplement, any agent will agree to use its reasonable best efforts to solicit purchases for the period of its appointment. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">We may sell the securities directly to institutional investors or others who may be deemed to be underwriters within the meaning of the
Securities Act with respect to any sale of those securities. We will describe the terms of any such sales in a prospectus supplement. </P> <P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B>Delayed Delivery
Contracts </B></P> <P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">We may authorize agents, underwriters or dealers to solicit offers from certain types of institutions to purchase securities
from us at the public offering price under delayed delivery contracts. These contracts would provide for payment and delivery on a specified date in the future. The contracts would be subject only to those conditions described in a prospectus
supplement. Such prospectus supplement will describe the commission payable for solicitation of those contracts. </P> <P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B>Remarketing </B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">We may offer and sell any of the securities in connection with a remarketing upon their purchase, in accordance with a redemption or repayment
by their terms or otherwise, by one or more remarketing firms acting as principals for their own accounts or as our agents. The name of any remarketing firm, the terms of any remarketing agreement and the compensation to be paid to the remarketing
firm will be included in a prospectus supplement, as required. Remarketing firms may be deemed to be underwriters within the meaning of the Securities Act. </P>
<P STYLE="margin-top:18pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B>Derivative Transactions </B></P> <P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">We may enter
into derivative transactions with third parties, or sell securities not covered by this prospectus to third parties in privately negotiated transactions. If any applicable prospectus supplement indicates, in connection with those derivatives, the
third parties may sell securities covered by this prospectus and the applicable prospectus supplement, including in short sale transactions then the third parties may use securities pledged by us or borrowed from us or others to settle those sales
or to close out any related open borrowings of securities, and may use securities received from us in settlement of those derivatives to close out any related open borrowings of securities. The third parties in these sale transactions will be
underwriters and will be identified in such applicable prospectus supplement or in a post-effective amendment to the registration statement of which this prospectus forms a part. </P>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">28 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman"><B>General Information </B></P>
<P STYLE="margin-top:6pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">In connection with the sale of the securities, underwriters, dealers or agents may be deemed to have received compensation from us in the form
of underwriting discounts or commissions and also may receive commissions from securities purchasers for whom they may act as agent. Underwriters may sell the securities to or through dealers, and the dealers may receive compensation in the form of
discounts, concessions or commissions from the underwriters or commissions from the purchasers for whom they may act as agent. We will provide in a prospectus supplement any required information regarding any underwriting discounts or other
compensation that we pay to underwriters or agents in connection with the securities offering, and any discounts, concessions or commissions that underwriters allow to dealers. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Any underwriters, dealers or agents participating in a distribution of the securities may be deemed to be underwriters within the meaning of
the Securities Act, and any discounts and commissions received by them and any profit realized by them on resale of the securities may be deemed to be underwriting discounts and commissions under the Securities Act. We may agree to indemnify
underwriters, dealers and agents who participate in the distribution of securities against certain liabilities to which they may become subject in connection with the sale of the securities, including liabilities arising under the Securities Act, or
to contribute with respect to payments that the agents, dealers or underwriters may be required to make because of those liabilities. Agents, dealers and underwriters, or their affiliates or associates, may be customers of, engage in transactions
with or perform services for us in the ordinary course of their businesses. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Other than our common stock, which is listed on the NYSE,
each series of offered securities will have no established trading market. We may elect to list any series of offered securities on an exchange, but we are not obligated to do so. It is possible that one or more underwriters may make a market in a
series of offered securities. However, they will not be obligated to do so and may discontinue market making at any time without notice. We cannot assure you as to the liquidity of, or the trading market for, any of our offered securities. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">To the extent required, this prospectus may be amended or supplemented from time to time to describe a specific plan of distribution. The
place and time of delivery for the securities in respect of which this prospectus is delivered may be set forth in a prospectus supplement, if required. </P>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">29 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center"><B><A NAME="toc326517_13"></A>LEGAL MATTERS </B></P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The validity of the securities offered by this prospectus and certain other legal matters will be passed upon for us by Baker Botts L.L.P.,
Houston, Texas. If certain legal matters in connection with an offering of the securities made by this prospectus are passed on by counsel for the underwriters of such offering, that counsel will be named in a prospectus supplement related to that
offering. </P> <P STYLE="margin-top:24pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center"><B><A NAME="toc326517_14"></A>EXPERTS </B></P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The financial statements and management&#146;s assessment of the effectiveness of internal control over financial reporting (which is included
in Management&#146;s Report on Internal Control over Financial Reporting) incorporated in this prospectus by reference to the Annual Report on Form <FONT STYLE="white-space:nowrap">10-K</FONT> for the year ended December&nbsp;31, 2019 have been so
incorporated in reliance on the report (which contains an explanatory paragraph on the effectiveness of internal control over financial reporting due to the exclusion of certain elements of the internal control over financial reporting of the seven
businesses the registrant acquired during 2019) of PricewaterhouseCoopers LLP, an independent registered public accounting firm, given on the authority of said firm as experts in auditing and accounting. </P>
<P STYLE="margin-top:24pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center"><B><A NAME="toc326517_15"></A>WHERE YOU CAN FIND MORE INFORMATION </B></P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">We have filed with the Securities and Exchange Commission a registration statement on Form <FONT STYLE="white-space:nowrap">S-3</FONT> under
the Securities Act with respect to the shares being offered under this prospectus. This prospectus, which is included in the registration statement, does not contain all of the information in the registration statement. For further information
regarding the company and our securities, please see the registration statement and our other filings with the Securities and Exchange Commission, including our annual, quarterly and current reports and proxy statements. Our filings with the
Securities and Exchange Commission are also available to the public on the Securities and Exchange Commission&#146;s Internet website at www.sec.gov. Our Internet website address is www.quantaservices.com. </P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">We furnish holders of our common stock with annual reports containing financial statements audited by our independent auditors in accordance
with generally accepted accounting principles following the end of each fiscal year. We file reports and other information with the Securities and Exchange Commission pursuant to the reporting requirements of the Securities Exchange Act of 1934, as
amended (the &#147;Exchange Act&#148;). </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Descriptions in this prospectus of documents are intended to be summaries of the material,
relevant portions of those documents, but may not be complete descriptions of those documents. For complete copies of those documents, please refer to the exhibits to the registration statement and other documents filed by us with the Securities and
Exchange Commission. </P> <P STYLE="margin-top:24pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center"><B><A NAME="toc326517_16"></A>INCORPORATION OF CERTAIN INFORMATION BY REFERENCE </B></P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">The Securities and Exchange Commission allows us to &#147;incorporate by reference&#148; the information we have filed with the Securities and
Exchange Commission, which means that we can disclose important information to you without actually including the specific information in this prospectus by referring you to those documents. The information incorporated by reference is an important
part of this prospectus, and later information that we file with the Securities and Exchange Commission will automatically update and supersede this information. Therefore, before you decide to invest in a particular offering under this shelf
registration, you should always check for reports we may have filed with the Securities and Exchange Commission after the date of this prospectus. We incorporate by reference into this prospectus the documents listed below, including the exhibits
</P>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">30 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman">
thereto, and any future filings we make with the Securities and Exchange Commission under Sections 13(a), 13(c), 14, or 15(d) of the Exchange Act until the applicable offering under this
prospectus and any applicable prospectus supplement is terminated, other than information furnished to the Securities and Exchange Commission under Item 2.02 or 7.01 of Form <FONT STYLE="white-space:nowrap">8-K</FONT> and which is not deemed filed
under the Exchange Act and is not incorporated in this prospectus: </P> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">our Annual Report on <A HREF="http://www.sec.gov/Archives/edgar/data/../../../ix?doc=/Archives/edgar/data/1050915/000105091520000020/pwr-123119x10k.htm">Form
 <FONT STYLE="white-space:nowrap">10-K</FONT></A> for the year ended December&nbsp;31, 2019, filed with the Securities and Exchange Commission on February&nbsp;28, 2020 (the &#147;Form <FONT STYLE="white-space:nowrap">10-K&#148;);</FONT>
</P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">our Quarterly Reports on Form <FONT STYLE="white-space:nowrap">10-Q</FONT> for the quarterly periods ended
March&nbsp;31, 2020 and June&nbsp;30, 2020, filed with the Securities and Exchange Commission on <A HREF="http://www.sec.gov/Archives/edgar/data/1050915/000105091520000073/pwr03-31x202010xq.htm">May&nbsp;
8, 2020</A> and <A HREF="http://www.sec.gov/Archives/edgar/data/1050915/000105091520000100/pwr06-30x202010xq.htm">August&nbsp;7, 2020</A>; </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">our Current Reports on Form <FONT STYLE="white-space:nowrap">8-K,</FONT> filed with the Securities and Exchange
Commission on <A HREF="http://www.sec.gov/Archives/edgar/data/1050915/000119312520094763/d909752d8k.htm">April&nbsp;1, 2020</A> and <A HREF="http://www.sec.gov/Archives/edgar/data/1050915/000119312520158581/d929978d8k.htm">June&nbsp;2, 2020</A>;
</P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">our <A HREF="http://www.sec.gov/Archives/edgar/data/1050915/000119312520109894/d822931ddef14a.htm">Definitive Proxy
 Statement</A> on Schedule 14A for our 2020 Annual Meeting of Stockholders, filed with the Securities and Exchange Commission on April&nbsp;17, 2020, to the extent incorporated by reference in Part III of the Form
<FONT STYLE="white-space:nowrap">10-K;</FONT> and </P></TD></TR></TABLE> <P STYLE="font-size:6pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<TABLE STYLE="BORDER-COLLAPSE:COLLAPSE; font-family:Times New Roman; font-size:10pt" BORDER="0" CELLPADDING="0" CELLSPACING="0" WIDTH="100%">
<TR style = "page-break-inside:avoid">
<TD WIDTH="5%">&nbsp;</TD>
<TD WIDTH="3%" VALIGN="top" ALIGN="left">&#149;</TD>
<TD WIDTH="1%" VALIGN="top">&nbsp;</TD>
<TD ALIGN="left" VALIGN="top"> <P ALIGN="left" STYLE=" margin-top:0pt ; margin-bottom:0pt; font-family:Times New Roman; font-size:10pt">our <A HREF="http://www.sec.gov/Archives/edgar/data/1050915/0000930661-98-000155.txt">Form <FONT
STYLE="white-space:nowrap">8-A12B</FONT></A>, filed with the Securities and Exchange Commission on January&nbsp;28, 1998, and any amendments or reports filed for the purpose of updating the description therein, including the description of our
capital stock filed as <A HREF="http://www.sec.gov/Archives/edgar/data/1050915/000105091520000020/pwr-ex41x12312019.htm">Exhibit 4.1</A> to our Form <FONT STYLE="white-space:nowrap">10-K.</FONT> </P></TD></TR></TABLE>
<P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">Any statement contained in a document incorporated by reference herein shall be deemed to be modified or superseded for all purposes to the
extent that a statement contained in this prospectus, or in any other subsequently filed document which is also incorporated or deemed to be incorporated by reference, modifies or supersedes such statement. Any statement so modified or superseded
shall not be deemed, except as so modified or superseded, to constitute a part of this prospectus. </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; text-indent:4%; font-size:10pt; font-family:Times New Roman">We will provide, without charge, to
each person to whom a copy of this prospectus has been delivered, including any beneficial owner, upon written or oral request of such person, a copy of any or all of the documents incorporated by reference herein (other than certain exhibits to
such documents not specifically incorporated by reference). Requests for such copies should be directed to: </P> <P STYLE="margin-top:12pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">2800 Post Oak Boulevard, Suite
2600 </P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">Houston, Texas 77056 </P>
<P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">(713) <FONT STYLE="white-space:nowrap">629-7600</FONT> </P>
<P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">Attention: Corporate Secretary </P>
 <p STYLE="margin-top:0pt;margin-bottom:0pt ; font-size:8pt">&nbsp;</P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center">31 </P>

</DIV></Center>


<p style="margin-top:1em; margin-bottom:0em; page-break-before:always">
<HR SIZE="3" style="COLOR:#999999" WIDTH="100%" ALIGN="CENTER">
<h5 align="left"><a href="#toc">Table of Contents</a></h5>


<Center><DIV STYLE="width:8.5in" align="left">
 <P STYLE="line-height:2.0pt;margin-top:0pt;margin-bottom:0pt;border-bottom:2.00pt solid #000000">&nbsp;</P>
<P STYLE="line-height:3.0pt;margin-top:0pt;margin-bottom:2pt;border-bottom:1px solid #000000">&nbsp;</P> <P STYLE="margin-top:72pt; margin-bottom:0pt; font-size:16pt; font-family:Times New Roman" ALIGN="center"><B>$1,500,000,000 </B></P>
<P STYLE="font-size:36pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P> <P STYLE="margin-top:0pt;margin-bottom:0pt" ALIGN="center">


<IMG SRC="https://ot-cdn.s3.us-west-2.amazonaws.com/filing/Archives/edgar/data/1050915/000119312521271415/g326517g12n84.jpg" ALT="LOGO">
 </P> <P STYLE="font-size:24pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P> <P STYLE="margin-top:24pt; margin-bottom:0pt; font-size:18pt; font-family:Times New Roman" ALIGN="center"><B>Quanta Services, Inc. </B></P>
<P STYLE="margin-top:24pt; margin-bottom:0pt; font-size:14pt; font-family:Times New Roman" ALIGN="center"><B>$500,000,000 0.950% Senior Notes due 2024 </B></P>
<P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:14pt; font-family:Times New Roman" ALIGN="center"><B>$500,000,000 2.350% Senior Notes due 2032 </B></P>
<P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:14pt; font-family:Times New Roman" ALIGN="center"><B>$500,000,000 3.050% Senior Notes due 2041 </B></P>
<P STYLE="margin-top:72pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center"><I>Joint Book-Running Managers </I></P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; font-size:12pt; font-family:Times New Roman" ALIGN="center"><B>BofA Securities </B></P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:12pt; font-family:Times New Roman" ALIGN="center"><B>Wells
Fargo Securities </B></P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:12pt; font-family:Times New Roman" ALIGN="center"><B>J.P. Morgan </B></P>
<P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:12pt; font-family:Times New Roman" ALIGN="center"><B>PNC Capital Markets LLC </B></P>
<P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:12pt; font-family:Times New Roman" ALIGN="center"><B>Truist Securities </B></P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center"><I>Senior Co-Managers </I></P>
<P STYLE="margin-top:12pt; margin-bottom:0pt; font-size:12pt; font-family:Times New Roman" ALIGN="center"><B>BBVA </B></P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:12pt; font-family:Times New Roman" ALIGN="center"><B>BMO Capital
Markets </B></P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:12pt; font-family:Times New Roman" ALIGN="center"><B>BNP PARIBAS </B></P>
<P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:12pt; font-family:Times New Roman" ALIGN="center"><B>Citizens Capital Markets </B></P>
<P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:12pt; font-family:Times New Roman" ALIGN="center"><B>MUFG </B></P> <P STYLE="margin-top:12pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center"><I>Co-Managers
</I></P> <P STYLE="margin-top:12pt; margin-bottom:0pt; font-size:12pt; font-family:Times New Roman" ALIGN="center"><B>HSBC </B></P> <P STYLE="margin-top:0pt; margin-bottom:0pt; font-size:12pt; font-family:Times New Roman" ALIGN="center"><B>US
Bancorp </B></P> <P STYLE="font-size:24pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P><center> <P STYLE="line-height:6.0pt;margin-top:0pt;margin-bottom:2pt;border-bottom:1.00pt solid #000000;width:21%">&nbsp;</P></center>
<P STYLE="margin-top:24pt; margin-bottom:0pt; font-size:10pt; font-family:Times New Roman" ALIGN="center"><B>The date of this prospectus supplement is September 9, 2021 </B></P> <P STYLE="font-size:30pt;margin-top:0pt;margin-bottom:0pt">&nbsp;</P>
<P STYLE="line-height:1.0pt;margin-top:0pt;margin-bottom:0pt;border-bottom:1px solid #000000">&nbsp;</P> <P STYLE="line-height:4.5pt;margin-top:0pt;margin-bottom:2pt;border-bottom:2.00pt solid #000000">&nbsp;</P>
</DIV></Center>

</BODY></HTML>
</TEXT>
</DOCUMENT>
</br></br></br>
'''

text = HTMLParser(target_html).text()

print(text)

if __name__ == '__main__':
    pass
