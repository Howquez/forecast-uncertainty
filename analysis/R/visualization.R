style <- theme(panel.border = element_blank(),
               panel.background = element_rect(fill = "white"),
               panel.grid.major = element_blank(),
               panel.grid.minor = element_blank(),
               # axis.line.x = element_line(size = 0.5, linetype = "solid",
               #                            colour = "black"),
               axis.text.y = element_blank(),
               axis.ticks.y = element_blank(),
               axis.title.y = element_blank())



p <- ggplot(data = main, aes(x = diff_BG, y = 0.33, col = location))
p + geom_jitter(width = 0.0, height = 0.33,
                alpha = 0.5) + # "#FC6100"
  ylim(0,5) +
  style

        

p <- ggplot(data = main, aes(x = prior_BG, col = location, fill = location))
p + geom_density(alpha = 0.5) +
  style + 
  scale_fill_manual(values=c(style_primary, style_secondary)) +
  scale_color_manual(values=c(style_primary, style_secondary))
