<ul>
    <li><%- ctx.postCount %> posts</li><span class='sep'>
    </span><li><%= ctx.makeFileSize(ctx.diskUsage) %></li><span class='sep'>
    </span><li>Build <a class='version' href='https://github.com/rororobby/szurubooru/commits/master'><%- ctx.version %></a> from <%= ctx.makeRelativeTime(ctx.buildDate) %></li><span class='sep'>
    </span><% if (ctx.canListSnapshots) { %><li><a href='<%- ctx.formatClientLink('history') %>'>History</a></li><span class='sep'>
    </span><% } %>
</ul>
