## test_server

<body><h3>users</h3>
<table border="1">
<tbody><tr>
<td>id</td>
<td>username</td>
</tr>

<tr>
<td>7</td>
<td>권일</td>
</tr>

<tr>
<td>2</td>
<td>김성곤</td>
</tr>

<tr>
<td>10</td>
<td>박근우</td>
</tr>

<tr>
<td>6</td>
<td>이가람</td>
</tr>

<tr>
<td>9</td>
<td>이진석</td>
</tr>

<tr>
<td>3</td>
<td>이창현</td>
</tr>

<tr>
<td>5</td>
<td>이현웅</td>
</tr>

<tr>
<td>8</td>
<td>정재훈</td>
</tr>

<tr>
<td>4</td>
<td>진승혁</td>
</tr>

</tbody></table>

<h3>groups</h3>
<table border="1">
<tbody><tr>
<td>id</td>
<td>name</td>
<td>user_set</td>
</tr>

<tr>
<td>1</td>
<td>모플</td>
<td>[&lt;User: 진승혁&gt;, &lt;User: 김성곤&gt;, &lt;User: 이가람&gt;, &lt;User: 이창현&gt;, &lt;User: 이현웅&gt;]</td>
</tr>

<tr>
<td>3</td>
<td>일정</td>
<td>[&lt;User: 박근우&gt;]</td>
</tr>

<tr>
<td>2</td>
<td>지도</td>
<td>[&lt;User: 권일&gt;, &lt;User: 이현웅&gt;, &lt;User: 정재훈&gt;]</td>
</tr>

</tbody></table>

<h3>places</h3>
<table border="1">
<tbody><tr>
<td>id</td>
<td>name</td>
<td>lnglat</td>
</tr>

<tr>
<td>1</td>
<td>101호</td>
<td></td>
</tr>

<tr>
<td>2</td>
<td>102호</td>
<td></td>
</tr>

<tr>
<td>3</td>
<td>스타벅스강남</td>
<td>11,11</td>
</tr>

</tbody></table>


<h3>meetings</h3>
<table border="1">
<tbody><tr>
<td>id</td>
<td>group</td>
<td>user_set</td>
<td>time</td>
<td>place</td>
<td>homework</td>
</tr>

<tr>
<td>1</td>
<td>모플</td>
<td>[&lt;User: 진승혁&gt;, &lt;User: 김성곤&gt;, &lt;User: 이가람&gt;, &lt;User: 이창현&gt;, &lt;User: 이현웅&gt;]</td>
<td>Oct. 10, 2015, 3:06 a.m.</td>
<td>스타벅스강남</td>
<td></td>
</tr>

<tr>
<td>2</td>
<td>지도</td>
<td>[&lt;User: 권일&gt;, &lt;User: 이현웅&gt;, &lt;User: 정재훈&gt;]</td>
<td>Oct. 10, 2015, 3:07 a.m.</td>
<td>101호</td>
<td></td>
</tr>

<tr>
<td>3</td>
<td>일정</td>
<td>[&lt;User: 박근우&gt;]</td>
<td>Oct. 10, 2015, 3:07 a.m.</td>
<td>102호</td>
<td></td>
</tr>

</tbody></table>

<h3>attendances</h3>
<table border="1">
<tbody><tr>
<td>meeting_id</td>
<td>username</td>
<td>time_arrival</td>
<td>islate</td>
<td>done_hw</td>

</tr>

<tr>
<td>1</td>
<td>김성곤</td>
<td>Oct. 10, 2015, 3:08 a.m.</td>
<td>False</td>
<td>True</td>
</tr>

<tr>
<td>1</td>
<td>이창현</td>
<td>Oct. 10, 2015, 3:08 a.m.</td>
<td>False</td>
<td>False</td>
</tr>

<tr>
<td>1</td>
<td>박근우</td>
<td>Oct. 10, 2015, 3:08 a.m.</td>
<td>False</td>
<td>False</td>
</tr>

<tr>
<td>1</td>
<td>이진석</td>
<td>Oct. 10, 2015, 3:08 a.m.</td>
<td>False</td>
<td>False</td>
</tr>

<tr>
<td>1</td>
<td>이가람</td>
<td>Oct. 10, 2015, 3:08 a.m.</td>
<td>False</td>
<td>False</td>
</tr>

</tbody></table>

</body>
